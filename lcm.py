#given two number m  and n write a program 
#to print the least common mutiple of no m and n

m = int(input())
n = int(input())

mini = min(m,n)
lcm = 0
for i in range(1,mini+1):
    if m % i == 0 and n % i == 0:    
        lcm = i

lcm = (m*n) // lcm
print(lcm)