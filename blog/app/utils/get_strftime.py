''' @File :get_strftime.py @Author:张宇 @Date :2020/8/9 11:01 @Desc : '''
from datetime import datetime
t = datetime.now()

def get_strftime(time):
    return '{}年{}月{}日 {}:{}'.format(time.year,time.month,time.day,time.hour,time.minute)