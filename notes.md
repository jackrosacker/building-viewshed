2024-06-21
- update:
  - Able to use subprocess.call() to call gdal
  - Might be some weirdnes with the output files, but they look cool!
  ![image](img/Screenshot_2024-06-21.png)
  (done with observer z and target z each set to 200ft I think)
- able to:
  - successfully export a sealevel-normalized bldg height raster
  - run gdal_viewshed in terminal, and output what seems like a legit viewshed
- struggling to:
  - translate the gdal call into python via either (1) gdal.ViewshedGenerate() or (2) subprocess.call()
- Next steps:
  - plan how to best run the gdal call from within a pipeline. Maybe it doesn't need to be run from python? Could string everything together via bash or other
2024-06-04
- wrote code through bldg footprint raster generation
- may need to (1) normalize building height pixels to actual building heights and (2) figure out if the background of the raster is going to be an issue since it seems to be a similar color to the tallest buildings

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
- [Install GDAL](https://mits003.github.io/studio_null/2021/07/install-gdal-on-macos/)
- Data
  - [NYBB](https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm)
  - [Land Cover 2010]()
  - [Building Footprints]()

