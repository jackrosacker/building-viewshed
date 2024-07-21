from pathlib import Path
import subprocess
import rasterio
import shapely
import pandas as pd
import geopandas as gpd

def generate_viewshed(
    in_file: Path | str,
    out_file: Path | str,
    observer_x: int | float,
    observer_y: int | float,
    observer_z: int | float,
    target_z: int | float = 1,
    max_dist: int | float = 79200,
    driver: str = "GTiff",
    
) -> int:
    """_summary_

    Args:
        in_file (Path | str): _description_
        out_file (Path | str): _description_
        observer_x (int | float): _description_
        observer_y (int | float): _description_
        observer_z (int | float): _description_
        target_z (int | float): _description_
        max_dist (int | float): _description_
        driver (str, optional): _description_. Defaults to "GTiff".

    Returns:
        int: return code, where 0 == success and 1 == failure
    """
    result = subprocess.call(
        [
            f"gdal_viewshed \
            -b 1 \
            -ox {observer_x} \
            -oy {observer_y} \
            -oz {observer_z} \
            -tz {target_z} \
            -md {max_dist} \
            -f {driver} \
            {in_file} \
            {out_file}",
        ],
        text=True,
        shell=True,
    )
    return result


def raster_to_polygon_gdf(in_file: Path | str) -> gpd.GeoDataFrame:
    # source: https://py.geocompx.org/05-raster-vector#sec-raster-to-polygons
    # may require a rasterio.open() call...
    # TODO: add comments to each section, from src link above
    shapes = rasterio.features.shapes(rasterio.band(in_file, 1))
    poly_list = list(shapes)
    
    geom = [shapely.geometry.shape(i[0]) for i in poly_list]
    geom = gpd.GeoSeries(geom, crs=in_file.crs)
    
    values = [i[1] for i in poly_list]
    values = pd.Series(values)
    
    result = gpd.GeoDataFrame({'value': values, 'geometry': geom})
    
    return result


def calculate_visible_features(viewshed_gdf: gpd.GeoDataFrame, gdf_to_intersect: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """_summary_

    Args:
        viewshed_gdf (gpd.GeoDataFrame): _description_
        gdf_to_intersect (gpd.GeoDataFrame): _description_

    Returns:
        gpd.GeoDataFrame: _description_
    """
    # filter viewshed to only include visible cells ('value' == 255)
    viewshed_gdf.query(expr="value > 0", inplace=True)

    # dissolve on visible cells
    viewshed_gdf.dissolve(by="value")

    # calculate intersection between viewshed gdf and rail feature buffer
    intersection = gpd.overlay(viewshed_gdf, gdf_to_intersect, how='intersection')
    
    return intersection