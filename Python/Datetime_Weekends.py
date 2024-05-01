from datetime import datetime, timedelta

start_date = input()
end_date = input()

start_date = datetime.strptime(start_date, "%d %b %Y")
end_date = datetime.strptime(end_date,"%d %b %Y")
print(start_date)
print(end_date)
saturday_count = 0
sunday_count = 0

for day_offset in range((end_date - start_date).days+1):
    current_date = start_date + timedelta(days = day_offset)
    if current_date.weekday() == 5:
        saturday_count += 1
    elif current_date.weekday() == 6:
        sunday_count +=1 

print("Saturday: {}".format(saturday_count))
print("Sunday: {}".format(sunday_count)) 
