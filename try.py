import datetime as dt
import sys
import calendar

month=[24,25,25,26,26,24,27,26,24,24,25,26]

aa=dt.date(2024,4,14)
a="4"
print(dt.datetime.strptime(a,"%m").strftime("%b"))
print(aa.day)