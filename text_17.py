import os
from datetime import date

from datetime import datetime

for filename in os.listdir('.'):
    path = os.path.join('.',filename)

    if os.path.isdir(path):
        file_type = 'DIR'
    elif os.path.isfile(path):
        file_type = 'FILE'

    size = os.path.getsize(path)

    time = os.path.getmtime(path)
    time = datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

    print(path,file_type,time,size)