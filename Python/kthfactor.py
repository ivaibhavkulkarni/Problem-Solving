n = int(input())
k = int(input())

factor = n 
count = 0

for i in range(1,n+1):
    if n % factor == 0:
        count +=1
        if count == k:
            print(factor)
            break
    factor -=1
if count < k:
    print(1)
