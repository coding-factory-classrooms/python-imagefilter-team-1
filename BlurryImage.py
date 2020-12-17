import os, cv2, GrayScale, DilatedImage, BlurryImage
from os import makedirs
import logger


def All_images_filter_blurry(path, dstpath):
    try:
        makedirs(dstpath)
        logger.log('new file has been created for blurry images')

    except:
        print("Directory already exist, images will be written in "+ dstpath+ " folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = BlurryImage.blur_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
            logger.log()
        except cv2.error as e:
            print(e)

def blur_filter(image_entry):
    try:
        blurImage = cv2.GaussianBlur(image_entry, (15, 15), 0)
        return blurImage
    except cv2.error as e:
        print(e)


