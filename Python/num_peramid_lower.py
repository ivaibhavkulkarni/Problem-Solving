n = int(input())


for i in range(n,0,-1):
    final = ""
    b = 1
    for j in range(i):
        if i == n or i == 2 or i == 1:
            final = final + str(b) + " "
            b+=1
        else:
            hollow = "  " * (j-1)
            final = "1 " + hollow + str(b)
            b+=1
    print(final)