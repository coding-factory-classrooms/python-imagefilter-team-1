import os, cv2, GrayScale, DilatedImage, BlurryImage
from os import makedirs

path = r'imgs'  # Source Folder
dstpath = r'modified_imgs'  # Destination Folder

try:
    makedirs(dstpath)

except:
    print("Directory already exist, images will be written in modified_imgs folder")

# Folder won't used
files = os.listdir(path)

for image in files:
    try:
        img = cv2.imread(os.path.join(path, image))
        img = GrayScale.gray_filter(img)
        img = BlurryImage.blur_filter(img)
        img = DilatedImage.dilated_image(img)
        cv2.imwrite(os.path.join(dstpath, image), img)
    except cv2.error as e:
        print(e)
