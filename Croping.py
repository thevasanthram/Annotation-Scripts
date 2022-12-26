from PIL import Image
from shutil import copyfile
import os, os.path
import glob
import cv2 as cv

#path="F:\Deevia\Some random shit\focused_164844838-stock-photo-man-enjoying-slice-of-pizza"
#dst = "F:\Deevia\Data_6\train1\filteredImages"

files =  glob.glob("C:/Users/shett/OneDrive/Desktop/train1/*.jpg")


for img in files:
    im = Image.open(img)
    width, height = im.size
    head, tail = os.path.split(img)
    print(img)
    if (width!=1920 or height!=1080):
        img = im.crop((0,0,1920,1080))
        img.save("C:/Users/shett/OneDrive/Desktop/train1/"+ tail)
        