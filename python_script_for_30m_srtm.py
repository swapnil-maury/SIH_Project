import requests
import os

def download_srtm_1x1(api_key, output_filename="srtm_30m_1x1.tif"):
    # Define a 1x1 degree bounding box (West, South, East, North)
    # Example coordinates: A 1x1 degree block in India (approx 111x111 km)
    west = 77.0
    south = 28.0
    east = 78.0
    north = 29.0
    
    # OpenTopography API endpoint for SRTM GL1 (1 arc-second / 30m)
    url = "https://portal.opentopography.org/API/globaldem"
    
    # Payload parameters matching the API specifications
    params = {
        "demtype": "SRTMGL1",
        "south": south,
        "north": north,
        "west": west,
        "east": east,
        "outputFormat": "GTiff",
        "API_Key": api_key
    }
    
    print(f"Requesting 30m SRTM DEM for bounding box: {west}, {south}, {east}, {north}...")
    
    # Stream the request to handle large file sizes efficiently
    response = requests.get(url, params=params, stream=True)
    
    if response.status_code == 200:
        with open(output_filename, 'wb') as file:
            # Download in 8KB chunks to prevent memory overload
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Success! Map saved locally as: {os.path.abspath(output_filename)}")
    else:
        print(f"Download failed. HTTP Status Code: {response.status_code}")
        print(f"Error details: {response.text}")

if __name__ == "__main__":
    # You must register for a free API key at: https://portal.opentopography.org/
    # Replace the string below with your actual API key
    MY_API_KEY = "8c53be0032cbb111a082b40202e624ab" 
    
    download_srtm_1x1(MY_API_KEY)