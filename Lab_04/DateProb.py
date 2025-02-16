import datetime

# Problem 1
time_now = datetime.datetime.now()
_5daysAgo = time_now - datetime.timedelta(days=5)
print("5 days ago date:", _5daysAgo)

# Problem 2
current_time = datetime.datetime.now()
tomorrow = current_time + datetime.timedelta(days=1)
yesterday = current_time - datetime.timedelta(days=1)

print("Yesterday's date:", yesterday)
print("Today's date: ", current_time)
print("Tomorrow's date: ", tomorrow)

# Problem 3
current_time = datetime.datetime.now()

print(current_time.replace(microsecond=0))

# Problem 4

year_1 = int(input("Input your year: "))
month_1 = int(input("input your month: "))
day_1 = int(input("Input your day: "))
hour_1 = int(input("Input your hour: "))
min_1 = int(input("Input your minute: "))
sec_1 = int(input("Input your second: "))
msec_1 = int(input("Input your microsecond: "))

year_2 = int(input("Input your year: "))
month_2 = int(input("input your month: "))
day_2 = int(input("Input your day: "))
hour_2 = int(input("Input your hour: "))
min_2 = int(input("Input your minute: "))
sec_2 = int(input("Input your second: "))
msec_2 = int(input("Input your microsecond: "))

time1 = datetime.datetime(year_1, month_1, day_1, hour_1, min_1, sec_1, msec_1)
time2 = datetime.datetime(year_2, month_2, day_2, hour_2, min_2, sec_2, msec_2)

time_diff = abs(time1 - time2)

print(time_diff.total_seconds())