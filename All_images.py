import os, cv2
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
    img = cv2.imread(os.path.join(path, image))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(dstpath, image), gray)
