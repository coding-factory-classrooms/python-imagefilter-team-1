import sys , BlurryImage, GrayScale, DilatedImage, All_images


args = sys.argv

for i in range(0, len(args)):
    arg = args[i]
    print(arg)
    if arg == '-i':
        if i + 1 < len(args):
            path = args[i + 1]
    elif arg == '-o':
        if i + 1 < len(args):
            dstpath = args[i + 1]

All_images.All_images_filter(path, dstpath)

