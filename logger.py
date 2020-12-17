from datetime import datetime

def log(msg, log_file):
    print(msg)
logFile = 'filter.log'

def log(msg, log_file):
    """
    function which allows to record in the file {filter.log} each passage in all the functions of the program and the dates and times of passage
    :param msg: message à afficher dans {filter.log} après le passage dans une fonction
    """
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formated = f'{timestamp} - {msg}'

    with open(log_file, 'a') as f:
        f.write('I was here : ' + formated + '\n')
        f.write('------\n')
