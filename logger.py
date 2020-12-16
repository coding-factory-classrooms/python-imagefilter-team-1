from datetime import datetime

logFile = 'filter.log'

def log(msg):
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formated = f'{timestamp} - {msg}'
    with open(logFile, 'a') as f:
        f.write(formated +'\n')

def dumpLog():
    try:
        with open(logFile, 'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f'Cannot open {logFile}. error= {e}')