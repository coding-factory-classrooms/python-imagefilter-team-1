import os, cv2, GrayScale, DilatedImage, BlurryImage
from os import makedirs


def All_images_filter_blurry(path, dstpath):
    try:
        makedirs(dstpath)

    except:
        print("Directory already exist, images will be written in modified_imgs folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = BlurryImage.blur_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)

def blur_filter(image_entry, blur):
    try:
        blurImage = cv2.GaussianBlur(image_entry, (blur, blur), 0)
        return blurImage
    except cv2.error as e:
        print(e)


