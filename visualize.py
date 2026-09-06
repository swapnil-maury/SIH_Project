# import rasterio
# from rasterio.plot import show
# import matplotlib.pyplot as plt

# # Open your downloaded SRTM GeoTIFF file
# with rasterio.open('srtm_30m_1x1.tif') as src:
#     fig, ax = plt.subplots(figsize=(10, 10))
#     # Render using a terrain colormap
#     show(src, ax=ax, title="SRTM 30m Elevation Grid", cmap="terrain")
#     plt.xlabel("Longitude")
#     plt.ylabel("Latitude")
#     plt.show()


import rasterio

# Open the GeoTIFF file
with rasterio.open('srtm_30m_1x1.tif') as src:
    
    # Read the first band (layer) of the image into a 2D NumPy array
    elevation_matrix = src.read(1)

    # 1. Inspecting the Grid Shape
    print("--- Grid Information ---")
    print(f"Total Rows and Columns: {elevation_matrix.shape}")
    
    # 2. Extracting a specific (X, Y, Height) coordinate
    # Let's pick a random pixel, for example, row 500, column 500
    row, col = 500, 500
    
    # Use Rasterio's spatial transform to get the exact Longitude (X) and Latitude (Y)
    lon, lat = src.xy(row, col)
    
    # Get the Height (Z) from the NumPy array
    height = elevation_matrix[row, col]
    
    print("\n--- Specific Point Data ---")
    print(f"Pixel Location : Row {row}, Col {col}")
    print(f"Longitude (X)  : {lon}")
    print(f"Latitude (Y)   : {lat}")
    print(f"Elevation (Z)  : {height} meters")