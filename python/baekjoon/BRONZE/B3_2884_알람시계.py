hour, minute = input().split(' ')
hour = int(hour)
minute = int(minute)

minute = minute - 45

if minute < 0:
    if hour == 0:
        hour = 23
        minute = 60 + minute
    else:    
        hour -= 1
        minute = 60 + minute

print(hour, minute)