import os, cv2, GrayScale, DilatedImage, BlurryImage
from os import makedirs


def All_images_filter_grey_scale(path, dstpath):
    try:
        makedirs(dstpath)

    except:
        print("Directory already exist, images will be written in modified_imgs folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = GrayScale.gray_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)

def gray_filter(image_entry):
    try:
        gray = cv2.cvtColor(image_entry, cv2.COLOR_BGR2GRAY)
        return gray
    except cv2.error as e:
        print(e)
