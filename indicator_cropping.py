from asyncio.windows_events import NULL
from tkinter import Image
from xml.dom import NamespaceErr
import xml.dom.minidom
import glob
from PIL import Image

import shutil
import os  

directory = 'C:/Users/User/Desktop/15_7_22/Karthik_new'
all_files = glob.glob(os.path.join(directory, "*.xml"))

DestinationDirectoryParent = "C:/Users/User/Desktop/15_7_22/annotated_indicators - Copy/"


your_list = []

for filename in all_files:
    print("filename: " , filename)
    docs = xml.dom.minidom.parse(filename)
    name = docs.getElementsByTagName("name")
    xmin = docs.getElementsByTagName("xmin")
    xmax = docs.getElementsByTagName("xmax")
    ymin = docs.getElementsByTagName("ymin")
    ymax = docs.getElementsByTagName("ymax")
    
    # print("Indicator name: " , name[0].firstChild.nodeValue)
    # print("xmin: " , xmin[0].firstChild.nodeValue)
    # print("xmax: " , xmax[0].firstChild.nodeValue)
    # print("ymin: " , ymin[0].firstChild.nodeValue)
    # print("ymax: " , ymax[0].firstChild.nodeValue)

    maxlenth = len(name)
    # print(maxlenth)

    nameOfImage = filename.replace(".xml" , ".jpg")
    # print("nameOfImage :" ,nameOfImage)

    im = Image.open(nameOfImage)

    for i in range(maxlenth):
        indicatorName = name[i].firstChild.nodeValue
        xmin_copy = xmin[i].firstChild.nodeValue
        ymin_copy = ymin[i].firstChild.nodeValue
        xmax_copy = xmax[i].firstChild.nodeValue
        ymax_copy = ymax[i].firstChild.nodeValue

        im1 = im.crop((int(xmin_copy) , int(ymin_copy), int(xmax_copy) , int(ymax_copy)))

        # im1.show()
        filenameNew = filename.replace(".xml" , '')
        filenameNew = filenameNew.replace(directory+'\\' , '')
        
        print(DestinationDirectoryParent+indicatorName+'/'+filenameNew+"_"+indicatorName+".jpg")


        im1.save(DestinationDirectoryParent+indicatorName+'/'+filenameNew+"_"+indicatorName+".jpg")



