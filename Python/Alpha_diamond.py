n = int(input())

alpha = 65
for i in range(1,n+1):
    if i == 1:
        print(" "*(n-i)+chr(alpha))
        alpha+=1
    else:
        spaces = " " * (n-i)
        hollow = " " *((i-1)*(2)-1)
        print(spaces + chr(alpha)+hollow + chr(alpha+1))
        alpha +=2

d_alpha = 65 + ((n*2)-4) 

for j in range(n-1,0,-1):
    if j == 1:
        print(" "*(n-j)+chr(d_alpha))
        d_alpha-=1
    else:
        spaces = " " *(n-j)
        hollow = " " * (((j-1)*2)-1)
        print(spaces + chr(d_alpha-1)+hollow + chr(d_alpha))
        d_alpha-=2