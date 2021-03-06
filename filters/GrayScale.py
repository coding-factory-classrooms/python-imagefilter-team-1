import os, cv2
from os import makedirs
import logger

def All_images_filter_grey_scale(path, dstpath, log_file):
    """
    This function is used to apply the {gray_filter()} function to all the images in a folder and create this folder if don't exist
    :param path: folder where to collect images
    :param dstpath: folder where to put the modified images
    """
    try:
        makedirs(dstpath)
        logger.log('new file "' + dstpath + '" has been created for gray images', log_file)

    except:
        print("Directory already exist, images will be written in "+ dstpath+ " folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = gray_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)
    logger.log('gray_filter function', log_file)
    print('gray_filter function')


def gray_filter(image_entry):
    """
    this function allows to put an image in black and white
    :param image_entry: image to filter
    :return: image with the filter applied
    """
    try:
        gray = cv2.cvtColor(image_entry, cv2.COLOR_BGR2GRAY)
        return gray
    except cv2.error as e:
        print(e)
