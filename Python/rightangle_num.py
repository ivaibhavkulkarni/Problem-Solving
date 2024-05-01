n = int(input())

a = 0
for i in range(n,0,-1):
    final = ""
    
    for j in range(1,i+1):
        a += 1
        if i == n or i == 2 or i == 1:
            final = final + str(a) + " "
        else:
            if j==1:
                final = final + str(a) + " "
            elif j==i:
                final = final + str(a)
            else:
                final+="  "
    print(final)