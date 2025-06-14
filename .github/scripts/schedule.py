import os
import requests
import pause
from datetime import datetime, timedelta
from multiprocessing import Pool

d = datetime.today().replace(hour=11, minute=0, second=0, microsecond=500)
t = timedelta((12 - d.weekday()) % 7)
d += t

print(d)
print(datetime.today() + timedelta((12 - d.weekday()) % 7))

cookie = os.environ["COOKIE"]

avail_dic = {"5AM": [7],
             "6AM": [7],
             "8AM": [4],
             "9AM": [2, 4, 5, 6],
             "10AM": [2, 4, 5, 6],
             "11AM": [4, 5],
             "12PM": [3, 4, 5, 6, 7],
             "1PM": [2, 3, 4, 5, 6]}

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