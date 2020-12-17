import os, cv2, logger
from filters import GrayScale, FilterZeTeam, BlurryImage, DilatedImage
from os import makedirs


def All_images_filter(path, dstpath, blur, iteration, log_file):

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
            img = FilterZeTeam.text_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)
    logger.log('All filters are applied', log_file)


def All_images_filter_dilate_blur(path, dstpath, blur, iteration, log_file):

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
    logger.log('Filter dilate and blur applied', log_file)


def All_images_filter_dilate_grayscale(path, dstpath, iteration, log_file):

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
    logger.log('Filters dilate and grayscale are applied', log_file)

def All_images_filter_dilate_grayscale_text(path, dstpath, iteration, log_file):

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
            img = FilterZeTeam.text_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)
    logger.log('Filter dilate grayscale and text are applied', log_file)

def All_images_filter_blur_grayscale(path, dstpath, blur, log_file):

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
    logger.log('Filters blur and grayscale are applied', log_file)

def All_images_filter_blur_grayscale_text(path, dstpath, blur, log_file):

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
            img = FilterZeTeam.text_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)
    logger.log('Filters blur, grayscale and text are applied', log_file)

def All_images_filter_text_gray(path, dstpath,log_file):

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
            img = FilterZeTeam.text_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)
    logger.log('Filters text and grayscale are applied', log_file)


def All_images_filter_text_blurry(path, dstpath, blur,log_file):

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
            img = FilterZeTeam.text_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)
    logger.log('Filters text and blur are applied', log_file)

def All_images_filter_dilated_text(path, dstpath, iteration, log_file):
    try:
        makedirs(dstpath)
    except:
        print("Directory already exist, images will be written in"+ dstpath+ "folder")

    # Folder won't used
    files = os.listdir(path)

    for image in files:
        try:
            img = cv2.imread(os.path.join(path, image))
            img = DilatedImage.dilated_image(img, iteration)
            img = FilterZeTeam.text_filter(img)
            cv2.imwrite(os.path.join(dstpath, image), img)
        except cv2.error as e:
            print(e)
    logger.log('Filters dilate and text are applied', log_file)

