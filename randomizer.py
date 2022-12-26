import os
import shutil
import glob
import random


dir = "C:/Users/Intern/Desktop/Teaser_Test_Datasets/"
folders = glob.glob(os.path.join(dir , "*"))

destinationFolder = 'C:/Users/Intern/Desktop/annotated_indicators - Copy/'

for folder in folders:
    images =  glob.glob(os.path.join(folder,"*.jpg"))
    random_list = random.sample(range(1,100),5)
    head, tail = os.path.split(folder)

    for i in range(5):
        singleImage = images[random_list[i]]

        print(singleImage)

        first, last = os.path.split(singleImage)
        
        # print("Destination Path: " , destinationFolder+tail+'/'+last)

        shutil.copy(singleImage , destinationFolder+tail+'/'+last)