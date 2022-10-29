import datetime

d1 = datetime.date(2021, 1, 9)
d1 = datetime.date.today()
print(d1.year)

from datetime import time

t1 = time(7, 15, 12, 3)
print(t1)
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print(datetime.datetime.weekday())