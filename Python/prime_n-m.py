m = int(input())
n = int(input())

for i in range(m,n+1):
    sum = 0
    for j in range(2,i):
        if i % j == 0:
            sum +=1
    if sum==0:
        print(i)