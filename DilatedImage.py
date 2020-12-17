import os, cv2, numpy
from os import makedirs
import logger

def All_images_filter_dilated(path, dstpath, iteration):
    try:
        makedirs(dstpath)
        logger.log('new file "' + dstpath + '" has been created for dilated images')

    except:
        print("Directory already exist, images will be written in"+ dstpath+ "folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = dilated_image(img, iteration)
            cv2.imwrite(os.path.join(dstpath, image), img)
            logger.log('All_images_filter_dilated function')
        except cv2.error as e:
            print(e)

def dilated_image(image_entry, iteration):


    try:
        kernel = numpy.ones((5, 5), numpy.uint8)
        newImg = cv2.dilate(image_entry, kernel, iterations=iteration)
        logger.log('dilated_image function')
        return newImg
    except cv2.error as e:
        print(e)
    except IndexError as e:
        print(e)
