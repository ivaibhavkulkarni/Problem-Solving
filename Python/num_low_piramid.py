m = int(input())
n = int(input())
x = m
z = 0
for i in range(n,0,-1):
    final = ""
    final = " " * (z)
    for j in range(1,i+1):
        if i == n or j == (j%2!=0):
            final = final + str(x) + " "
            x+=1
        elif j == i :
            final += str(x) + " "
            x+=1
        else:
            final += "  "
            x+=1
    print(final)
    z+=1