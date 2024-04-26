# to know how many mondays comes in 1ST

from datetime import datetime

year_input = input().split()
start_year = int(year_input[0])
end_year = int(year_input[1])

mondays = 0
months = range(1,13)
for year in range(start_year,end_year+1):
    for month in months:
        date_time_object = datetime(year,month,1)
        name_of_week = datetime.strftime(date_time_object,"%A")
        if name_of_week == "Monday":
            mondays += 1
print(mondays)