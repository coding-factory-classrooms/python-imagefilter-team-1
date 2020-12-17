from datetime import datetime

logFile = 'filter.log'

def log(msg):
    f"""
    function which allows to record in the file {filter.log} each passage in all the functions of the program and the dates and times of passage
    :param msg: message à afficher dans {filter.log} après le passage dans une fonction
    """
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formated = f'{timestamp} - {msg}'

    with open(logFile, 'a') as f:
        f.write('I was here : ' + formated + '\n')
        f.write('------\n')
