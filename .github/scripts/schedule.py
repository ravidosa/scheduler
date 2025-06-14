import os
import requests
import pause
from datetime import datetime, timedelta
from multiprocessing import Pool

d = datetime.today().replace(hour=11, minute=21, second=0, microsecond=500)
t = timedelta((12 - d.weekday()) % 7)
d += t

print(d)

cookie = os.environ["COOKIE"]
print(cookie)

avail_dic = {3: [2, 3],
             4: [2, 3, 4, 5, 6, 7],
             5: [2, 3, 4, 5, 6, 7],
             6: [3, 4, 6, 7],
             7: [3, 5, 6, 7],
             8: [2, 3, 5, 6, 7]}

def schedule(shift):
    hour, day = shift
    url = f"https://prv.tutor.com/nGEN/Tools/ScheduleManager_v2/SchedulerWorker.aspx?Type=Set&Week={d.month}/{d.day}/{d.year}&WeekDay={day}&Hour={hour}AM"
    x = requests.post(url, headers = {"Cookie": cookie})
    print("OS = ", os.environ.keys())
    print(x.headers)

if __name__ == '__main__':
    pool = Pool()
    pause.until(d)
    pool.map(schedule, [(hour, day) for hour in avail_dic for day in avail_dic[hour]])
    pool.close()