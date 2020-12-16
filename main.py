import sys , BlurryImage, GrayScale, DilatedImage, All_images

filter_dictionnary = {}
args = sys.argv
path = None
dstpath = None

for i in range(0, len(args)):
    arg = args[i]
    if arg == '-h':
        print('usage: imagefilter\n'
              '-h, ----help\n'
              '-i, --input-dir <directory>\n'
              '-o, --output-dir <directory>')
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
            print(tab_filters)
            for filter in tab_filters:
                filter_split = filter.split(':')
                try:
                    filter_dictionnary[filter_split[0]] = filter_split[1]
                except IndexError as e:
                    filter_dictionnary[filter_split[0]] = ''

print(filter_dictionnary)
if path == None:
    print("There is no directory initialised")
elif dstpath == None:
    dstpath = 'default_directory'
else:
    All_images.All_images_filter(path, dstpath)

