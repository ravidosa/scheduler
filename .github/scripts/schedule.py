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

avail_dic = {"10AM": [6],
             "11AM": [2, 6],
             "12PM": [2, 4, 5, 6],
             "1PM": [2, 4, 5],
             "2PM": [2, 4, 5, 6],
             "3PM": [4, 5, 6],
             "4PM": [2, 4, 6],
             "5PM": [4, 5, 6],
             "6PM": [2, 4, 5, 6],}

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