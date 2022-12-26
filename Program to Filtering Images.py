#from hashlib import new
from PIL import Image
from shutil import copyfile
import os, os.path
import glob
import cv2 as cv

path=r'F:\Deevia\Data_6\train'
def filterImages(path, thresholdWidth, thresholdHeight):
	
	
    imgs = []

   
    valid_images = [".jpg"]
    

    
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]

        if ext.lower() not in valid_images:
            continue
        imgs.append(f)

	
    directory = os.path.join(path, 'filteredImages')
    print("dir",directory)
    if not os.path.exists(directory):
        os.makedirs(directory)

	
    filteredImages = []
	
    for i in imgs:
        image = Image.open(os.path.join(path, i))
        width, height = image.size

		
        if ((width != thresholdWidth) or (height != thresholdHeight)):
            
            
            src_xml_ = os.path.splitext(i)[0] + ".xml"
            src_xml = os.path.join(path, src_xml_)
            basename = os.path.splitext(os.path.basename(i))[0]
            dst_xml = os.path.join(path + '/filteredImages',basename +".xml")
            
            
            src = os.path.join(path, i)
            dst = os.path.join(path + '/filteredImages',i)
            #read_file = Image.open(dst)
            image=image.crop((0,0,1920,1080)) 
            image.save(i)
            #new_img=image.crop((0,0,1920,1080))
            #print(path+"/"+i)
            
            #new_img.save(dst)
            print("src",src)
            print("dst",dst)
           
            copyfile(src,dst)
            copyfile(src_xml,dst_xml)
		
        filteredImages.append(i)
    return filteredImages




if __name__ == '__main__':
	
	filteredImages = [ ]
	
	
	filteredImages = filterImages(r"F:\Deevia\Data_6\train1", 1920, 1080) 

dst = "F:\Deevia\Data_6\train1\filteredImages"

files =  glob.glob((filteredImages,"*.jpg"))



    


