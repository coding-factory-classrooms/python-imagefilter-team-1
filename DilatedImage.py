import cv2
import numpy

def dilated_image(image_entry):

    try:
        image = cv2.imread(image_entry)
        newImg = cv2.split(image)[0]
        (retVal, newImg) = cv2.threshold(newImg, 130, 255, cv2.THRESH_BINARY)
        kernel = numpy.ones((6, 6), numpy.uint8)
        newImg = cv2.dilate(newImg, kernel, iterations=1)
        cv2.imwrite('dilated_imgs/8-Mile.jpg', newImg)
    except cv2.error as e:
        print(e)
    except IndexError as e:
        print(e)

dilated_image('imgs/8-Mile.jpg')
