"""
Satellite Imagery Fetch + Validation (Corrected)
------------------------------------------------
Fetches Sentinel-1 SAR (GRD, VV) imagery from the Copernicus Data Space
Ecosystem (CDSE) for a bounding box + date range, then validates the
downloaded .tif to confirm:
  1. It opens correctly (not corrupted/empty).
  2. Its geographic bounds actually match the bbox you requested
     (this is the real "correct location" check - not the preview image).
  3. Its pixel statistics look like real SAR data (not all-zero/NaN).
  4. A properly-stretched (dB + percentile) preview so it's actually
     visible, instead of the earlier all-black image.

Install dependencies:
    pip install requests rasterio numpy matplotlib --break-system-packages
"""

import json
import requests
import numpy as np
import rasterio
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# CONFIG - fill these in
# ---------------------------------------------------------------------
CDSE_USERNAME = "kumarsatyam87832@gmail.com" 
CDSE_PASSWORD = "Vea-WRxwKNw73B5"

# (min_lon, min_lat, max_lon, max_lat)
BBOX = (88.30, 26.40, 88.50, 26.60)

START_DATE = "2024-07-01"
END_DATE = "2024-07-15"

OUT_TIF = "sentinel1_vv_backscatter.tif"
OUT_PREVIEW = "tif_preview_fixed.png"


# ---------------------------------------------------------------------
# STEP 1: Authenticate
# ---------------------------------------------------------------------
def get_access_token(username: str, password: str) -> str:
    url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
    data = {
        "client_id": "cdse-public",
        "username": username,
        "password": password,
        "grant_type": "password",
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]


# ---------------------------------------------------------------------
# STEP 2: Search for available Sentinel-1 GRD products (metadata only)
# ---------------------------------------------------------------------
def search_sentinel1_products(bbox: tuple, start_date: str, end_date: str) -> list:
    min_lon, min_lat, max_lon, max_lat = bbox

    aoi_polygon = (
        f"POLYGON(({min_lon} {min_lat}, {max_lon} {min_lat}, "
        f"{max_lon} {max_lat}, {min_lon} {max_lat}, {min_lon} {min_lat}))"
    )

    filter_query = (
        f"Collection/Name eq 'SENTINEL-1' and "
        f"Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' "
        f"and att/OData.CSC.StringAttribute/Value eq 'GRD') and "
        f"OData.CSC.Intersects(area=geography'SRID=4326;{aoi_polygon}') and "
        f"ContentDate/Start gt {start_date}T00:00:00.000Z and "
        f"ContentDate/Start lt {end_date}T00:00:00.000Z"
    )

    url = "https://catalogue.dataspace.copernicus.eu/odata/v1/Products"
    params = {"$filter": filter_query, "$top": 20}

    response = requests.get(url, params=params)
    response.raise_for_status()
    products = response.json().get("value", [])

    print(f"Found {len(products)} Sentinel-1 GRD product(s) for the given bbox/date range.")
    for p in products:
        print(f"  - {p['Name']}  (sensed: {p['ContentDate']['Start']})")

    return products


# ---------------------------------------------------------------------
# STEP 3: Pull the actual SAR raster via Sentinel Hub Process API
# ---------------------------------------------------------------------
def fetch_sar_raster(token: str, bbox: tuple, start_date: str, end_date: str,
                      width: int = 512, height: int = 512) -> bytes:
    min_lon, min_lat, max_lon, max_lat = bbox

    evalscript = """
    //VERSION=3
    function setup() {
      return {
        input: ["VV"],
        output: { bands: 1, sampleType: "FLOAT32" }
      };
    }
    function evaluatePixel(sample) {
      return [sample.VV];
    }
    """

    payload = {
        "input": {
            "bounds": {
                "bbox": [min_lon, min_lat, max_lon, max_lat],
                "properties": {"crs": "http://www.opengis.net/def/crs/EPSG/0/4326"},
            },
            "data": [
                {
                    "type": "sentinel-1-grd",
                    "dataFilter": {
                        "timeRange": {
                            "from": f"{start_date}T00:00:00Z",
                            "to": f"{end_date}T23:59:59Z",
                        },
                        "acquisitionMode": "IW",
                        "polarization": "DV",
                    },
                }
            ],
        },
        "output": {
            "width": width,
            "height": height,
            "responses": [{"identifier": "default", "format": {"type": "image/tiff"}}],
        },
        "evalscript": evalscript,
    }

    url = "https://sh.dataspace.copernicus.eu/api/v1/process"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()

    return response.content


# ---------------------------------------------------------------------
# STEP 4: Validate the downloaded .tif
# ---------------------------------------------------------------------
def validate_tif(path: str, expected_bbox: tuple, preview_out: str,
                  bbox_tolerance_deg: float = 0.01):
    print(f"\nValidating: {path}")

    # --- Open check ---
    try:
        with rasterio.open(path) as src:
            data = src.read(1).astype(np.float32)
            bounds = src.bounds
            crs = src.crs
    except Exception as e:
        print("FAILED TO OPEN FILE - download likely corrupted/incomplete.")
        print(f"Error: {e}")
        return

    print("File opened successfully.")
    print(f"  CRS          : {crs}")
    print(f"  File bounds  : {bounds}")
    print(f"  Expected bbox: {expected_bbox}")

    # --- Location check: compare file bounds vs requested bbox ---
    min_lon, min_lat, max_lon, max_lat = expected_bbox
    location_ok = (
        abs(bounds.left - min_lon) <= bbox_tolerance_deg
        and abs(bounds.bottom - min_lat) <= bbox_tolerance_deg
        and abs(bounds.right - max_lon) <= bbox_tolerance_deg
        and abs(bounds.top - max_lat) <= bbox_tolerance_deg
    )
    print(f"  Location match (within {bbox_tolerance_deg} deg): "
          f"{'PASS' if location_ok else 'FAIL - bbox mismatch, check request params'}")

    # --- Pixel statistics ---
    total_pixels = data.size
    nan_count = int(np.isnan(data).sum())
    zero_count = int(np.sum(data == 0))
    print("\nPixel statistics:")
    print(f"  Min / Max / Mean : {np.nanmin(data):.4f} / {np.nanmax(data):.4f} / {np.nanmean(data):.4f}")
    print(f"  NaN pixels       : {nan_count} ({100*nan_count/total_pixels:.2f}%)")
    print(f"  Zero pixels      : {zero_count} ({100*zero_count/total_pixels:.2f}%)")

    data_ok = True
    if nan_count == total_pixels or zero_count == total_pixels:
        print("  ISSUE: image is entirely empty/NaN - request likely failed silently.")
        data_ok = False
    if np.nanstd(data) < 1e-6:
        print("  ISSUE: no variation in pixel values - not a real scene.")
        data_ok = False

    if location_ok and data_ok:
        print("\nOVERALL: Imagery appears valid and correctly located.")
    else:
        print("\nOVERALL: Issues found - re-check bbox/date range or re-download.")

    # --- Corrected visualization: dB conversion + percentile stretch ---
    data_db = 10 * np.log10(np.where(data > 0, data, np.nan))
    vmin, vmax = np.nanpercentile(data_db, [2, 98])

    plt.figure(figsize=(6, 6))
    plt.imshow(data_db, cmap="gray", vmin=vmin, vmax=vmax)
    plt.colorbar(label="Backscatter (dB)")
    plt.title("SAR Preview (dB, percentile-stretched)")
    plt.axis("off")
    plt.savefig(preview_out, dpi=150, bbox_inches="tight")
    print(f"\nSaved corrected preview to: {preview_out}")


# ---------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("Authenticating with CDSE...")
    token = get_access_token(CDSE_USERNAME, CDSE_PASSWORD)
    print("Authenticated.\n")

    print("Searching for Sentinel-1 GRD products...")
    products = search_sentinel1_products(BBOX, START_DATE, END_DATE)

    if not products:
        print("No products found - try widening the date range.")
    else:
        print("\nFetching SAR raster...")
        raster_bytes = fetch_sar_raster(token, BBOX, START_DATE, END_DATE)

        with open(OUT_TIF, "wb") as f:
            f.write(raster_bytes)
        print(f"Saved raster to {OUT_TIF}")

        validate_tif(OUT_TIF, BBOX, OUT_PREVIEW)