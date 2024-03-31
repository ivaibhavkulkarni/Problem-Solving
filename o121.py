n = int(input())

for i in range(1,n+1):
    final = ""
    for j in range(1,i+1):
        final = final + str(j)
    for k in range(i-1,0,-1):
        final = final + str(k)
    print(final)