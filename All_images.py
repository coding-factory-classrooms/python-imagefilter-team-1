import os, cv2, GrayScale, DilatedImage, BlurryImage
from os import makedirs


def All_images_filter(path, dstpath, blur, iteration):

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
            img = BlurryImage.blur_filter(img, blur)
            img = DilatedImage.dilated_image(img, iteration)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)

def All_images_filter_dilate_blur(path, dstpath, blur, iteration):

    try:
        makedirs(dstpath)

    except:
        print("Directory already exist, images will be written in modified_imgs folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = BlurryImage.blur_filter(img, blur)
            img = DilatedImage.dilated_image(img, iteration)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)

def All_images_filter_dilate_grayscale(path, dstpath, iteration):

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
            img = DilatedImage.dilated_image(img, iteration)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)

def All_images_filter_blur_grayscale(path, dstpath, blur):

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
            img = BlurryImage.blur_filter(img, blur)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)