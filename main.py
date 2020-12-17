import sys, BlurryImage, GrayScale, DilatedImage, All_images

filter_dictionnary = {}
args = sys.argv
path = None
dstpath = None
blur = None
iteration = None
grayscale= None

for i in range(0, len(args)):
    arg = args[i]
    if arg == '-h':
        print('usage: imagefilter\n'
              '-h, ----help\n'
              '-i, --input-dir <directory>\n'
              '-o, --output-dir <directory>\n'
              '--filters, --filters "grayscale|dilate:X|blur:X"')
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



if path == None:
    print("There is no directory initialised")
elif dstpath == None:
    dstpath = 'default_directory'
elif (iteration == None) & (blur == None) & (grayscale == ''):
    GrayScale.All_images_filter_grey_scale(path, dstpath)
elif (iteration == None) & (grayscale == None) & (blur != None):
    blur = int(blur)
    if ((blur % 2) == 0) | (blur < 0):
        print('The blur need to be positive and odd')
    else:
        BlurryImage.All_images_filter_blurry(path, dstpath, blur)
elif (iteration != None) & (grayscale == None) & (blur == None):
    iteration = int(iteration)
    DilatedImage.All_images_filter_dilated(path, dstpath, iteration)
elif (iteration != None) & (grayscale == None) & (blur != None):
    iteration = int(iteration)
    blur = int(blur)
    if ((blur % 2)== 0) | (blur < 0):
        print('The blur need to be positive and odd')
    else:
        All_images.All_images_filter_dilate_blur(path, dstpath, blur, iteration)
elif (iteration == None) & (grayscale == '') & (blur != None):
    blur = int(blur)
    if ((blur % 2) == 0) | (blur < 0):
        print('The blur need to be positive and odd')
    else:
        All_images.All_images_filter_blur_grayscale(path, dstpath, blur)
elif (iteration != None) & (grayscale == '') & (blur == None):
    iteration = int(iteration)
    All_images.All_images_filter_dilate_grayscale(path, dstpath, iteration)
else:
    blur = int(blur)
    iteration = int(iteration)
    if ((blur % 2) == 0) | (blur < 0):
        print('The blur need to be positive and odd')
    else:
        All_images.All_images_filter(path, dstpath, blur, iteration)
