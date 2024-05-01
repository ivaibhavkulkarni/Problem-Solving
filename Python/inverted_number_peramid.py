s = int(input())
n = int(input())

k = 0
for i in range(1,n+1):
    k+=i
num=k+s-1
for j in range(1,n+1):
    final =""
    for v in range(j):
        final = final + str(num)+" "
        num -=1
    print(final)