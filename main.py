import sys
import BlurryImage
import GrayScale
import DilatedImage


GrayScale.gray_filter()
BlurryImage.blur_filter()
DilatedImage.dilated_image()

args = sys.argv

for i in range(0, len(args)):
    arg = args[i]
    print(arg)
    if arg == '--grayscale':
        print('')
    elif arg == '--dilated':
        print('')
