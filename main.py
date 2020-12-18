import sys, All_images, logger, initfile, os
from filters import GrayScale, BlurryImage, DilatedImage
from os import listdir


filter_dictionnary = {}
args = sys.argv
path = None
dstpath = None
blur = None
iteration = None
grayscale= None
text =None
log_file = 'filter.log'

for i in range(0, len(args)):
    arg = args[i]
    if arg == '-h':
        print('usage: imagefilter\n'
              '-h, ----help\n'
              '-i, --input-dir <directory>\n'
              '-o, --output-dir <directory>\n'
              '--filters, --filters "grayscale|dilate:X|blur:X|text"\n'
              '--log, --log-file filter.log\n'
              '--config-file, --config-file image.ini\n'
              '--list-filters, give the list of all the filters')
    elif arg == '-i':
        if i + 1 < len(args):
            path = args[i + 1]
    elif arg == '-o':
        if i + 1 < len(args):
            dstpath = args[i + 1]
    elif arg == '--filters':
        if i + 1 < len(args):
            filters = args[i + 1]
            tab_filters = filters.split('|')
            for filter in tab_filters:
                filter_split = filter.split(':')
                try:
                    filter_dictionnary[filter_split[0]] = filter_split[1]
                except IndexError as e:
                    filter_dictionnary[filter_split[0]] = ''
            for key in filter_dictionnary.keys():
                if key == 'blur':
                    blur = filter_dictionnary[key]
                elif key == 'dilate':
                    iteration = filter_dictionnary[key]
                elif key == 'grayscale':
                    grayscale = filter_dictionnary[key]
                elif key == 'text':
                    text_filter = filter_dictionnary[key]
    elif arg == '--log-file':
        if i + 1 < len(args):
            log_file = args[i + 1]
    elif arg == '--config-file':
        if i + 1 < len(args):
            doc_ini = args[i + 1]
            initfile.default_parameters(doc_ini)
    elif arg == '--list-filters':
        filters_package = listdir('filters')
        for filter_file in filters_package:
            file_extension = os.path.splitext(filter_file)[1]
            if file_extension == '.py':
                print(' - ' + filter_file.replace('.py', ''))

if len(args) == 1:
    initfile.default_parameters('filter.ini')
elif path == None:
    print('No initialized directory')
elif dstpath == None:
    dstpath = 'default_directory'
elif (iteration == None) and (blur == None) and (grayscale == '') and (text == ''):
    All_images.All_images_filter_text_gray(path, dstpath, log_file)
elif (iteration == None) and (blur == None) and (grayscale == '') and (text == None):
    GrayScale.All_images_filter_grey_scale(path, dstpath, log_file)
elif (iteration == None) and (grayscale == None) and (blur != None) and (text == None):
    blur = int(blur)
    if ((blur % 2) == 0) or (blur < 0):
        print('The blur need to be positive and odd')
    else:
        BlurryImage.All_images_filter_blurry(path, dstpath, blur, log_file)
elif (iteration == None) and (grayscale == None) and (blur != None) and (text == ''):
    blur = int(blur)
    if ((blur % 2) == 0) or (blur < 0):
        print('The blur need to be positive and odd')
    else:
        All_images.All_images_filter_text_blurry(path, dstpath, blur, log_file)
elif (iteration != None) and (grayscale == None) and (blur == None) and (text == None):
    iteration = int(iteration)
    DilatedImage.All_images_filter_dilated(path, dstpath, iteration, log_file)
elif (iteration != None) and (grayscale == None) and (blur == None) and (text == ''):
    iteration = int(iteration)
    All_images.All_images_filter_dilated_text(path, dstpath, iteration, log_file)
elif (iteration != None) and (grayscale == None) and (blur != None) and (text == None):
    iteration = int(iteration)
    blur = int(blur)
    if ((blur % 2)== 0) or (blur < 0):
        print('The blur need to be positive and odd')
    else:
        All_images.All_images_filter_dilate_blur(path, dstpath, blur, iteration, log_file)
elif (iteration != None) and (grayscale == None) and (blur != None) and (text == ''):
    iteration = int(iteration)
    blur = int(blur)
    if ((blur % 2)== 0) or (blur < 0):
        print('The blur need to be positive and odd')
    else:
        All_images.All_images_filter_dilate_blur_text(path, dstpath, blur, iteration, log_file)
elif (iteration == None) and (grayscale == '') and (blur != None) and (text == None):
    blur = int(blur)
    if ((blur % 2) == 0) or (blur < 0):
        print('The blur need to be positive and odd')
    else:
        All_images.All_images_filter_blur_grayscale(path, dstpath, blur, log_file)
elif (iteration == None) and (grayscale == '') and (blur != None) and (text == ''):
    blur = int(blur)
    if ((blur % 2) == 0) or (blur < 0):
        print('The blur need to be positive and odd')
    else:
        All_images.All_images_filter_blur_grayscale_text(path, dstpath, blur)
elif (iteration != None) and (grayscale == '') and (blur == None) and (text == None):
    iteration = int(iteration)
    All_images.All_images_filter_dilate_grayscale(path, dstpath, iteration)
elif (iteration != None) and (grayscale == '') and (blur == None) and (text == ''):
    iteration = int(iteration)
    All_images.All_images_filter_dilate_grayscale_text(path, dstpath, iteration)
else:
    blur = int(blur)
    iteration = int(iteration)
    if ((blur % 2) == 0) or (blur < 0):
        print('The blur need to be positive and odd')
    else:
        All_images.All_images_filter(path, dstpath, blur, iteration)
