from datetime import datetime

logFile = 'filter.log'

def log(msg):
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formated = f'{timestamp} - {msg}'

    with open(logFile, 'a') as f:
        f.write('je suis passé par ici : ' + formated + '\n')
        f.write('------\n')


# def dumb_log():
#     try:
#         f = open(logFile, 'r')
#         print(f.read())
#         f.close()
#     except FileNotFoundError as e:
#         print(f'cannot open {logFile}. error={e}')