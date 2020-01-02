# -*- coding: utf-8 -*-
import os

rasterfiles = []
def listdir(path):
    global rasterfiles
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path)
        elif os.path.splitext(file_path)[1]=='.tif':
             rasterfiles.append(file_path)
    return rasterfiles

sourdir = 'D:/tif/yunnan'

def buildoverview(sourdir):
    rasterfiles = listdir(sourdir)
    for r in rasterfiles:
        ovrfile = r + '.ovr'
        if not os.path.exists(ovrfile):
            print( r + '----创建ovr')
            cmd_s = 'gdaladdo ' + r + ' -r nearest -ro 2 4 8 16'
            result = os.popen(cmd_s)
            print(result.readline())

buildoverview(sourdir)