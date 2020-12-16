import cv2

def blur_filter(image_entry):
    try:
        blurImage = cv2.GaussianBlur(image_entry, (15, 15), 0)
        return blurImage
    except cv2.error as e:
        print(e)


