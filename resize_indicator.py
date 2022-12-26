from PIL import Image
import glob
import os

directory = 'C:/Users/User/Desktop/15_7_22/annotated_indicators - Copy/'
new_size = (64,64)

for folder in glob.glob(os.path.join(directory , '*')):
    all_files = glob.glob(os.path.join(folder, "*.jpg"))
    for file in all_files:
        image = Image.open(file)
        img_width, img_height = image.size
        if img_height == img_width:
            im1 = image.resize(new_size)
        elif (img_height > img_width):
            result = Image.new(image.mode, (img_height, img_height), (0,0,0))
            result.paste(image, ((img_height - img_width) // 2, 0))
            im1 = result.resize(new_size)
        elif (img_width > img_height):
            result = Image.new(image.mode, (img_width, img_width), (0,0,0))
            result.paste(image, (0, (img_width - img_height) // 2))
            im1 = result.resize(new_size)
        im1.save(file)
