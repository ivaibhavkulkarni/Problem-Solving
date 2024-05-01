m = int(input())
n = int(input())
a = 1
for i in range(m):
    final = ""
    for j in range(n):
        if i == 0 or i == m-1:
            final = final + str(a) + " "
            a+=1
        else:
            if j == 0 or j == n-1:
                hollow = " " * ((n*2)-3)
                final = final + str(a) + hollow 
            a+=1
    print(final)