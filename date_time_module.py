
import datetime as dt

now = dt.datetime.now()
print(now, type(now))


year = now.year
print(year, type(year))

month = now.month
print(month, type(month))

weekday = now.weekday()
print(weekday, type(weekday))

date_of_birth = dt.datetime(year=1979, month=1, day=2)
print(date_of_birth)
