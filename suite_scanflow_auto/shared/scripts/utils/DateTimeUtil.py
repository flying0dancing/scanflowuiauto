
import time,datetime
from time import strftime

def get_time():
    now = time.localtime()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S",now)
    return now_time

def get_dateYYYMMDD():
    now = time.localtime()
    now_time = time.strftime("%Y%m%d",now)
    return now_time

if __name__ == '__main__':
    now_time = get_dateYYYMMDD()
    print(now_time)