import cv2

def blur_filter():
    image = cv2.imread('imgs/8-Mile.jpg')
    blurImage = cv2.GaussianBlur(image, (15, 15), 0)

    cv2.imwrite('blur_imgs/8-Mile.jpg', blurImage)