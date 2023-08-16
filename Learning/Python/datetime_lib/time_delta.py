import datetime

delta_time = datetime.timedelta(days=3, hours=5, minutes=8, seconds=10)
print(delta_time.days, delta_time.seconds, delta_time.microseconds, delta_time.total_seconds())
print('*' * 20)
delta_time = datetime.timedelta(days=100)
date_now = datetime.datetime.now()
print('Now :', date_now)
print('After 100 days :', date_now + delta_time)