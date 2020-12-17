import os, cv2
from os import makedirs
import logger

def All_images_filter_grey_scale(path, dstpath):
    try:
        makedirs(dstpath)
        logger.log('new file "' + dstpath + '" has been created for gray images')

    except:
        print("Directory already exist, images will be written in "+ dstpath+ " folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = gray_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
            logger.log('All_images_filter_grey_scale function')
        except cv2.error as e:
            print(e)

def gray_filter(image_entry):
    try:
        gray = cv2.cvtColor(image_entry, cv2.COLOR_BGR2GRAY)
        logger.log('gray_filter function')
        return gray
    except cv2.error as e:
        print(e)
