# -*- coding: utf-8 -*-
import os
# 遍历文件夹下所有影像文件，拿到所有影像文件的路径
# 截取原始文件路径——拼接输出文件路径
# 执行重投影命令

# gdalwarp -t_srs EPSG:4326 -r near -of GTiff 
# E:/Work/data/湖滏小流域/影像/DOM_NAD/E119D5_N31D2_20190316_ZY02C_HR1_DOM/E119D5_N31D2_20190316_ZY02C_HR1_DOM.tif E:/Work/data/湖滏小流域/wrap/测试.tif

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

sourdir = 'E:/Work/data/hufu/raster'

target_dir = 'E:/Work/data/hufu/wrap'
cmd_shell = 'gdalwarp -t_srs EPSG:4326 -r near -of GTiff '

def wrapwgs84(sourdir):
    rasterfiles = listdir(sourdir)
    for r in rasterfiles:
        r = r.replace('\\','/')
        idnex = r.find('raster') + 6
        tail = r[idnex:]
        target_file = target_dir + tail
        mkdir(os.path.dirname(target_file))
        cmd_s = cmd_shell + r + ' ' + target_file
        result = os.popen(cmd_s)
        print(result)
        
 
def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)         #makedirs 创建文件时如果路径不存在会创建这个路径
		print("---  new folder...  ---")
		print("---  OK  ---")
	else:
		print("There is this folder!")
wrapwgs84(sourdir)


