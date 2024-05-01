m = int(input())
n = int(input())
for i in range(1,m+1):
    final = ""
    k=7
    for j in range(1,n+1):
        if i == 1 or i == m:
            final = final + str(k) + " "
            k +=1
        else:
            if j == 1 or j == n:
                final = final + str(k) + " "
                k+=1
            else:
                final = final + "  "
                k+=1
    print(final)    
