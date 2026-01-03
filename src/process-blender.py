from cartoHD import run_command, cartoHDprocess
import os

BASE = "tmp/es/"

INPUT = BASE + "input/*.laz"
OUTPUT = BASE + "output/"

os.makedirs(OUTPUT, exist_ok=True)

cartoHDprocess(
    input_lidar_data=INPUT,
    output_folder=OUTPUT,
    bounds=None,      # use full tiles
    margin=0,
    case="ES",        # Spain (building class = 6)
    override=True,
    forBlender=True
)
