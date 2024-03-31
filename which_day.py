# d is the day which the month is starting from and 
# and the number is nTH day will be ?




d = input()
n = int(input())

if d == "Sunday":
    day = 1
elif d == "Monday":
    day = 2
elif d == "Tuesday":
    day = 3
elif d == "Wednesday":
    day = 4
elif d == "Thursday":
    day = 5
elif d == "Friday":
    day = 6
elif d == "Saturday":
    day =7


new_date = (n-1) + day
new_day = new_date % 7

if new_day == 1:
    print("sun")
elif new_day == 2:
    print("mon")
elif new_day == 3:
    print("tue")
elif new_day == 4:
    print("wed")
elif new_day == 5:
    print("thur")
elif new_day == 6:
    print("fri")
elif new_day == 7:
    print("sat")


