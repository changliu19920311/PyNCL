#!/usr/bin/env python3
# ==============================================================================
# Author: Feng Zhu
# Date: 2015-01-26 12:23:30
__version__ = '0.0.1'
# ==============================================================================

# import os
import subprocess


class NCL:

    def create(file_path, ncl_code):
        ncl_file = open(file_path, 'w')
        ncl_file.write(ncl_code)
        ncl_file.close()

    def run(file_path):
        subprocess.call('ncl ' + file_path, shell=True)


class Func:

    def wrf_user_getvar(wrfout_path, var):
        file_path = 'tmp.ncl'
        # wrfout_path = 'wrfout.nc'
        # var = 'slp'
        ncl_code = '''
load "$NCARG_ROOT/lib/ncarg/nclscripts/wrf/WRFUserARW.ncl"

begin

f = addfile("''' + wrfout_path + '''","r")
lat2d = f->XLAT(0, :, :)
lon2d = f->XLONG(0, :, :)
dims = dimsizes(lat2d)
nlat  = dims(0)
nlon  = dims(1)

time = 0
var = wrf_user_getvar(f, "''' + var + '''", time)

opt = True
opt@fout = "''' + var + '''.dat"
fmt = nlon + "f15.9"
write_matrix(var, fmt, opt)

end
    '''

        NCL.create(file_path, ncl_code)
        NCL.run(file_path)
