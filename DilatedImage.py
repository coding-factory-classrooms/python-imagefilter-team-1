import os, cv2, GrayScale, DilatedImage, BlurryImage, numpy
from os import makedirs


def All_images_filter_dilated(path, dstpath):
    try:
        makedirs(dstpath)

    except:
        print("Directory already exist, images will be written in"+ dstpath+ "folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = DilatedImage.dilated_image(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)

def dilated_image(image_entry):

    try:
        newImg = cv2.split(image_entry)[0]
        (retVal, newImg) = cv2.threshold(newImg, 130, 255, cv2.THRESH_BINARY)
        kernel = numpy.ones((6, 6), numpy.uint8)
        newImg = cv2.dilate(newImg, kernel, iterations=1)
        return newImg
    except cv2.error as e:
        print(e)
    except IndexError as e:
        print(e)

dilated_image('imgs/8-Mile.jpg')