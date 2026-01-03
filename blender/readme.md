## For Blender 5.0

Blender needs images instead of GeoTiffs, so we adjust the process a bit.

Here are the exact Anaconda / Conda commands, in the correct order, for CartoHD + Blender export on Windows.

1️⃣ Create the environment
conda create -n cartohd python=3.11 -y

2️⃣ Activate it
conda activate cartohd


You should now see:

(cartohd)

3️⃣ Install core geo stack (CRITICAL: conda-forge)
conda install -c conda-forge -y ^
  gdal ^
  pdal ^
  numpy ^
  scipy ^
  rasterio ^
  geopandas ^
  shapely ^
  fiona ^
  pyproj


⚠️ Do not use pip for GDAL / Fiona / Rasterio on Windows

4️⃣ Verify binaries (important sanity check)
gdalinfo --version
pdal --version


Both must print versions (no errors).

5️⃣ Run CartoHD

From the CartoHD root folder:

python src\process-blender.py

6️⃣ (Optional) Blender-only reruns

After your changes, you can safely rerun with:

forBlender=True
override=False


in process-blender.py.

7️⃣ (Optional) Export again manually

If you ever need to re-export the heightmap:

gdal_translate ^
  -ot UInt16 ^
  -scale ^
  -a_nodata none ^
  -of PNG ^
  tmp\es\output\dtm.tif ^
  tmp\es\output\dtm_height.png

TL;DR
conda create -n cartohd python=3.11 -y
conda activate cartohd
conda install -c conda-forge gdal pdal numpy scipy rasterio geopandas shapely fiona pyproj -y
python src\process-blender.py