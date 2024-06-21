# imports
from pathlib import Path
import geopandas as gpd

# initialize paths etc.
url = "https://data.cityofnewyork.us/api/geospatial/qb5r-6dgf?method=export&format=Shapefile"
data_path = Path("data")

# pull down bldg shp via url
bldg_gdf = gpd.read_file(filename=url, engine="pyogrio")

out_data_name = "buildings"
file_ext = "parquet"

# to_crs 2263
bldg_gdf.to_crs(epsg="2263",inplace=True)
# export gdf as geoparquet
bldg_gdf.to_parquet(data_path / f"{out_data_name}.{file_ext}")

