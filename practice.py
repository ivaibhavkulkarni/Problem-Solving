string = input()

sum_a = 0
n = 0
for i in string:
    if i.isdigit():
        sum_a += int(i)
        n += 1
        average = sum_a / n

print(sum_a)
print(round(average,2))