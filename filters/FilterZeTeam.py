import os, cv2
from os import makedirs
import logger

def All_images_filter_text_filter(path, dstpath):
    """
    This function is used to apply the {text_filter()} function to all the images in a folder and create this folder if don't exist
    :param path: folder where to collect images
    :param dstpath: folder where to put the modified images
    """
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
            img = text_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
            logger.log('All_images_filter_grey_scale function')
        except cv2.error as e:
            print(e)


def text_filter(image_entry):
    """
    this function allows to add text to an image, you can configure the font family, size and color
    :param image_entry: image to filter
    :return: image with the filter applied
    """
    position = (10,50)
    new_img= cv2.putText(image_entry,
          'Leo.G/ Maxime.L', #text
          position, #position at which writing has to start
          cv2.FONT_HERSHEY_SIMPLEX, #font family
          1, #font size
          (209, 80, 0, 255), #font color
          3) #font stroke
    return new_img
