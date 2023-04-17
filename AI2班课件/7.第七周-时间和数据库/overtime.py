import time
import datetime


birthday = datetime.datetime(year=2003, month=1, day=5).timestamp()
print(birthday)
end_date = datetime.datetime(year=2103, month=10, day=10).timestamp()
print(end_date)
print(end_date - birthday)
while True:
    now = datetime.datetime.now().timestamp()
    time.sleep(1)
    print(f"年轻人, 你还剩下{end_date-now}秒可以挥霍")