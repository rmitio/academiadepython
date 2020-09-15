import datetime
segundos = int(input())

hms = str(datetime.timedelta(seconds=segundos))
print(hms)