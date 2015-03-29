#!/usr/bin/env python3
# ==============================================================================
# Author: Feng Zhu
# Date: 2015-01-26 12:23:30
__version__ = '0.0.1'
# ==============================================================================

import os
import subprocess

work_dir = os.getcwd()
tmp_dir = os.path.join(work_dir, '.pyncl')

if not os.path.isdir(tmp_dir):
    os.mkdir(tmp_dir)


class NCL:

    def create(file_path, ncl_code):
        ncl_file = open(file_path, 'w')
        ncl_file.write(ncl_code)
        ncl_file.close()

    def run(file_path):
        subprocess.call('ncl ' + file_path, shell=True)


class Func:

    def wrf_user_getvar(wrfout_path, var):
        ncl_file_path = os.path.join(tmp_dir, 'tmp.ncl')
        output_path = os.path.join(tmp_dir, var + '.dat')
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
opt@fout = "''' + output_path + '''"
fmt = nlon + "f15.9"
write_matrix(var, fmt, opt)

end
    '''
        NCL.create(ncl_file_path, ncl_code)
        NCL.run(ncl_file_path)


class Plot:

    def plot_track_error(track_errors, output_path):
        ncl_file_path = os.path.join(tmp_dir, 'tmp.ncl')
        ncl_code = '''
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"

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
opt@fout = "''' + output_path + '''"
fmt = nlon + "f15.9"
write_matrix(var, fmt, opt)

end
    '''
        NCL.create(ncl_file_path, ncl_code)
        NCL.run(ncl_file_path)
