from datetime import datetime, timedelta

current_date = input()
d_format = "%b %d %Y %I:%M %p"
date_obj = datetime.strptime(current_date, d_format)
NY = datetime(date_obj.year+1, 1, 1)
dt = NY-date_obj
h = dt.days*24 + dt.seconds//3600 
m = (dt.seconds//60) % 60
print("{} hours {} minutes".format(h, m))