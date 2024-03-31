n = int(input())
for i in range(1,n+1):
    i = str(i)
    p = len(i)
    sum = 0
    for j in i:
        j = int(j)
        sum += (j**p)

    if sum == int(i):
        print(sum) 