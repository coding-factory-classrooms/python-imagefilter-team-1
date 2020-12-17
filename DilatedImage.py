import os, cv2, GrayScale, BlurryImage, numpy
from os import makedirs


def All_images_filter_dilated(path, dstpath, iteration):
    try:
        makedirs(dstpath)

    except:
        print("Directory already exist, images will be written in modified_imgs folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = dilated_image(img, iteration)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)

def dilated_image(image_entry, iteration):


    try:
        kernel = numpy.ones((5, 5), numpy.uint8)
        newImg = cv2.dilate(image_entry, kernel, iterations=iteration)
        return newImg
    except cv2.error as e:
        print(e)
    except IndexError as e:
        print(e)

