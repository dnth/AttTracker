from datetime import date, time
import datetime


current_date = datetime.datetime.date(datetime.datetime.now())
current_time = datetime.datetime.time(datetime.datetime.now().replace(microsecond=0))
print current_date
print current_time
print type(current_date)
print type(current_time)



current_date = date(2015,9,6)
current_time = time(9,0,0)
print current_date
print current_time
print type(current_date)
print type(current_time)