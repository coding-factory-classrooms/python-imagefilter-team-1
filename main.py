import cv2

def gray_filter():
    image = cv2.imread('imgs/8-Mile.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('gray_imgs/8-Mile.jpg', gray)

def blur_filter():
    image = cv2.imread('imgs/8-Mile.jpg')
    blurImage = cv2.GaussianBlur(image, (15, 15), 0)

    cv2.imwrite('blur_imgs/8-Mile.jpg', blurImage)

gray_filter()
blur_filter()