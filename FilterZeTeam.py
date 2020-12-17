import os, cv2, FilterZeTeam
from os import makedirs
import logger

def All_images_filter_text_filter(path, dstpath):
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
            img = FilterZeTeam.text_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
            logger.log('All_images_filter_grey_scale function')
        except cv2.error as e:
            print(e)

def text_filter(image_entry):

     position = (10,50)
     new_img= cv2.putText(image_entry, #numpy array on which text is written
          'Leo.G/ Maxime.L', #text
          position, #position at which writing has to start
          cv2.FONT_HERSHEY_SIMPLEX, #font family
          1, #font size
          (209, 80, 0, 255), #font color
          3) #font stroke
     return new_img

All_images_filter_text_filter('imgs', 'imgas_new')