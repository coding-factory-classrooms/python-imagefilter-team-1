import os, cv2, numpy
from os import makedirs
import logger

def All_images_filter_dilated(path, dstpath, iteration, log_file):
    """
    This function is used to apply the {dilated_image()} function to all the images in a folder and create this folder if don't exist
    :param path: folder where to collect images
    :param dstpath: folder where to put the modified images
    :param iteration: number of times the pixels should dilate
    """
    try:
        makedirs(dstpath)
        logger.log('new file "' + dstpath + '" has been created for dilated images', log_file)

    except:
        print("Directory already exist, images will be written in"+ dstpath+ "folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = dilated_image(img, iteration)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)
    logger.log('dilated_image function', log_file)
    print('dilated_image function')

def dilated_image(image_entry, iteration):
    """
    this function allows to add a dilated filter to an image
    :param image_entry: image to filter
    :param iteration: number of times the pixels should dilate
    :return: image with the filter applied
    """

    try:
        kernel = numpy.ones((5, 5), numpy.uint8)
        newImg = cv2.dilate(image_entry, kernel, iterations=iteration)
        return newImg
    except cv2.error as e:
        print(e)
    except IndexError as e:
        print(e)
