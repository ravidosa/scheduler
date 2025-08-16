import os
import requests
import pause
from datetime import datetime, timedelta
from multiprocessing import Pool

d = datetime.today().replace(hour=16, minute=0, second=0, microsecond=500)
t = timedelta((12 - d.weekday()) % 7)
d += t

print(d)

cookie = os.environ["COOKIE"]

avail_dic = {"12AM": [3],
             "1AM": [3],
             "3AM": [1],
             "4AM": [1],
             "5AM": [1],
             "6AM": [1],
             "7PM": [5, 6],
             "8PM": [5, 6],
             "9PM": [2, 5, 6],
             "10PM": [2, 5, 6],
             "11PM": [2, 5, 6],}

def schedule(shift):
    hour, day = shift
    url = f"https://prv.tutor.com/nGEN/Tools/ScheduleManager_v2/SchedulerWorker.aspx?Type=Set&Week={d.month}/{d.day}/{d.year}&WeekDay={day}&Hour={hour}"
    x = requests.post(url, headers = {"Cookie": cookie})
    print(x.text)

if __name__ == '__main__':
    pool = Pool()
    pause.until(d)
    pool.map(schedule, [(hour, day) for hour in avail_dic for day in avail_dic[hour]])
    pool.close()