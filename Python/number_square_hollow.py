n = int(input())

for i in range(1,n+1):
    final = ""
    for j in range(n,0,-1):
        if i == 1 or  i == n:
            final = final + str(j) + " "
        else:
            if j < n and not j == 1:
                hollow = " " * (2)
                final = final + hollow
            else: 
                final = final + str(j) +" "
    print(final) 