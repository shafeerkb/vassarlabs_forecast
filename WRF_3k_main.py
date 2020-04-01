#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:05:40 2020

@author: vassar
"""

from pathlib import Path
import numpy as np
import pandas as pd
import xarray as xr
import metpy.calc as mpcalc
from metpy.units import units
import numpy as np
import pandas as pd
import xesmf as xe
import glob
import time
import os


import sys
sys.path.append("./src")
#import config


from WRF_3km_INDIA import WRF3km_fn,heatmap


sys.path.append("/home/vassar/Documents/forecast_vassarlabs/data")

in_file_path="/home/vassar/Documents/forcastdata/WRF/"
out_file_path="/home/vassar/Documents/forecast_vassarlabs/2020022600"
slice_hr=6
ref_date='2020-02-26 00:00:00'

WRF3km_fn(in_file_path,out_file_path,slice_hr,ref_date)   

    



