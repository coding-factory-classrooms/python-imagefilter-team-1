from configparser import ConfigParser
import All_images , logger


def default_parameters(doc_ini):
    filter_dictionnary = {}
    parser = ConfigParser()
    parser.read(doc_ini)

    input = parser.get('default', 'input_dir')
    output = parser.get('default', 'output_dir')
    log_file = parser.get('default', 'log_file')

    content = parser.get('filters', 'content')

    tab_filters = content.split('|')
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
                text = filter_dictionnary[key]

    All_images.All_images_filter(input, output, int(blur), int(iteration))
    logger.dumb_log()

