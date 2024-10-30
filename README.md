Python Tools for HDF4-EOS Format
================================

Unfortunately, many important NASA datasets are still distributed as HDF4-EOS granules. This small library may help you to avoid needing to install GDAL just to read the file. It is capable of reading an an HDF4 file (and HDF4-EOS files, in particular) and writing out a spatial dataset using `rasterio`, based on some strict assumptions about the file-level attributes; assumptions that are usually satisfied by an HDF4-EOS file.
