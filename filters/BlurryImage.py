import os, cv2
from os import makedirs
import logger


def All_images_filter_blurry(path, dstpath, blur):
    f"""
    This function is used to apply the {blur_filter()} function to all the images in a folder and create this folder if don't exist
    :param path: folder where to collect images
    :param dstpath: folder where to put the modified images
    :param blur: desired blur intensity
    """
    try:
        makedirs(dstpath)
        logger.log('new file "'+ dstpath+'" has been created for blurry images')

    except:
        print("Directory already exist, images will be written in "+ dstpath+ " folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = blur_filter(img, blur)
            cv2.imwrite(os.path.join(dstpath, image), img)
            logger.log('All_images_filter_blurry function')
        except cv2.error as e:
            print(e)

def blur_filter(image_entry, blur):
    """
    this function blurs an image
    :param image_entry: image to blur
    :param blur: desired blur intensity
    :return: image with the filter applied
    """
    try:
        blurImage = cv2.GaussianBlur(image_entry, (blur, blur), 0)
        logger.log('blur_filter function')
        return blurImage
    except cv2.error as e:
        print(e)


