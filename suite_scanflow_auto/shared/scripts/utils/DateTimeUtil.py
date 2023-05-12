import time,datetime
import os.path
from time import strftime

def get_time():
    now = time.localtime()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S",now)
    return now_time

def get_dateYYYMMDD():
    now = time.localtime()
    now_time = time.strftime("%Y%m%d",now)
    return now_time



'''
return None if the fname doesn't match cszx/mp4's name rule, ex. fname='smoke_1.0.9.301[2023-04-24T10-33-51][1.0.9.301].cszx' result: 2023-04-24
'''
def getDateByFileSuffix(fname):
    pics_fname = os.path.splitext(fname)
    #print(pics_fname[0])
    if pics_fname[1]=='.mp4':
        format="%Y%m%d%H%M%S%f"
    else:
        format = "%Y-%m-%dT%H-%M-%S"
    if '[' in pics_fname[0]:
        pics_f = pics_fname[0].split('[', 2)
        datetime_str = pics_f[1].replace(']','')
        if 'T' in datetime_str:
            format = "%Y-%m-%dT%H-%M-%S"
        datetime_result=datetime.datetime.strptime(datetime_str,format).date()
    else:
        datetime_result=None
    return datetime_result

def getDiffDays(fname):
    date1str=getDateTimeOfFile(fname)
    date2str=get_time()
    date1=datetime.datetime.strptime(date1str,"%Y-%m-%d %H:%M:%S")
    date2=datetime.datetime.strptime(date2str, "%Y-%m-%d %H:%M:%S")
    duration=date2-date1
    return duration.days

def getDateTimeOfFile(fname):
    ctime=os.path.getmtime(fname)
    return timeStampToTime(ctime)

def timeStampToTime(timestamp):
    timeStruct=time.localtime(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)

if __name__ == '__main__':
    #now_time = get_dateYYYMMDD()
    #print(now_time)
    getDiffDays(r'V:\Lion\Kun Shen\storage02_Kun Shen\result_scanflow\automaticTest\cszx\2_2[2023-04-27T14-33-02][1.0.9.301].cszx')

    
