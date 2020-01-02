import os

datadir = r'C:\Users\chenjl\Desktop\testdata'
listpath = r'C:\Users\chenjl\Desktop\testdata\imgList.txt'

def trans_img2tif(img_path):
    out_put = img_path[:-3]+"tif"
    os.popen("")

def createOverview(tif_path):
    out_put = tif_path + '.ovr'
    os.popen("")

f = open(listpath,'r')
nums = f.readlines()
f.close()
for num in nums:
    img_name = num.strip('\n')
    print(img_name)
    folderName = "DOM_" + img_name
    img_path = os.path.join(datadir,folderName,folderName+".img")
    print(img_path)
    tif_path = os.path.join(datadir,folderName,folderName+".tif")
    if not os.path.exists(tif_path):
        trans_img2tif(img_path)
        print(img_name + 'translated from img to tif')
        ovr_path = tif_path + '.ovr'
        if not os.path.exists(ovr_path):
            createOverview(tif_path)
            print(img_name + 'created overview')