2024-06-04
- wrote code through bldg footprint raster generation
- may need to (1) normalize building height pixels to actual building heights and (2) figure out if the background of my raster is going to be an issue since it seems to be a similar color to my tallest buildings

2024-06-03
- was able to load bldg footprints to geoparquet, and had initial success with converting vector to raster
- need to resolve:
  - potential crs issue with output GTIFF
  - are raster values correct in output GTIFF
### Resources:
- [geo1015](https://3d.bk.tudelft.nl/courses/backup/geo1015/2020/les/)
  - [associated book](https://github.com/tudelft3d/terrainbook/releases)
- [GDAL viewshed](https://gdal.org/programs/gdal_viewshed.html)
- [Line of Sight Analysis in Python](https://spatial-dev.guru/2023/12/10/line-of-sight-analysis-in-digital-elevation-models-using-python/)
- [Rasterize Vectors w. Rasterio](https://pygis.io/docs/e_raster_rasterize.html)
- Data
  - [NYBB](https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm)
  - [Land Cover 2010]()
  - [Building Footprints]()

