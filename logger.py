from datetime import datetime

def log(msg, log_file):
    print(msg)
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formated = f'{timestamp} - {msg}'

    with open(log_file, 'a') as f:
        f.write('I was here : ' + formated + '\n')
        f.write('------\n')
