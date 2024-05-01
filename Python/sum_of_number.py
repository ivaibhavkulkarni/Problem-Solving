n = int(input())
counter = 0 
sum_of_number = 0

while counter < n:
    sum_of_number += counter + 1
    counter = counter + 1

sum = sum_of_number / n
print(sum)



#### another way solving this problem
n = int(input())
counter = 0 
sum_of_number = 0 

while counter < n:
    counters = counter + 1
    sum_of_number = counters + sum_of_number
    counter = counter + 1

print(sum_of_number)
a = sum_of_number / n  
print(a) 