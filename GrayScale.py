import cv2

def gray_filter(image_entry):
    try:
        gray = cv2.cvtColor(image_entry, cv2.COLOR_BGR2GRAY)
        return gray
    except cv2.error as e:
        print(e)
