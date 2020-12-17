import os, cv2
from os import makedirs
import logger


def All_images_filter_blurry(path, dstpath, blur, log_file):
    try:
        makedirs(dstpath)
        logger.log('new file "'+ dstpath+'" has been created for blurry images', log_file)

    except:
        print("Directory already exist, images will be written in "+ dstpath+ " folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = blur_filter(img, blur)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)
    logger.log('blur_filter function', log_file)


def blur_filter(image_entry, blur):
    try:
        blurImage = cv2.GaussianBlur(image_entry, (blur, blur), 0)
        return blurImage
    except cv2.error as e:
        print(e)


