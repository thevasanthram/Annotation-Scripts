from asyncio.windows_events import NULL
import glob
from itertools import count
import os

Imagedirectory = 'C:/Users/User/Desktop/15_7_22/Data_4_indicator_cropped_image/eco_mode_indicator_light' #directory of images whose indicator should be replaced
all_image = glob.glob(os.path.join(Imagedirectory, "*.jpg")) 

xmldirectory = 'C:/Users/User/Desktop/15_7_22/Data_4' #directory of xmls whose indicator name should be replaced
all_xmls = glob.glob(os.path.join(xmldirectory , '*.xml'))

count = 0

for singleImage in all_image:
    head , tail = os.path.split(singleImage)
    singleImageName=''

    for i in range(len(tail)):
        if tail[i] == '_':
            singleImageName = tail[:i]
            break
    
    singleImageName = singleImageName + '.xml'
    # print("singleImageName with xml:" , singleImageName)

    correspodingXMLDirectory = xmldirectory + '/' + singleImageName
    # print('Corresponding XML directory: ', correspodingXMLDirectory)

    f = open(correspodingXMLDirectory , 'r')
    fileContent = f.read()
    f.close()

    # print('fileContent before replacing:' ,fileContent)

    if "fort_fort_eco_mode_indicator_light" in fileContent:
        fileContent = fileContent.replace('fort_fort_eco_mode_indicator_light' , 'fort_eco_mode_indicator_light')
        count = count + 1

    f = open(correspodingXMLDirectory , 'w')
    f.write(fileContent)
    f.close()
    # print('fileContent after replacing:' ,fileContent)

if(count > 0):
    print("Report: No file with eco_mode_indicator_light Found")
else:
    print("Report: {count} Files replaced with fort_eco_mode_indicator_light")
    