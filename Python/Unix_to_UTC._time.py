from datetime import datetime

n = int(input())
final_date = datetime.utcfromtimestamp(n)
print(final_date)