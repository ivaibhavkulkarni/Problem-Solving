m = int(input())
n = int(input())
if m < 2:
    m = 2
for i in range(m,n+1):
    sum = 0 
    for j in range(2,int(i**(0.5))+1):
        if i % j == 0:
            sum+=1
    if sum ==0:
        print(i)
        break
if sum!=0:
    print("not a prime")
