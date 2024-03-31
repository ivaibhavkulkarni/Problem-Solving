n = int(input())

for i in range(1,n+1):
    if i == 1:
        print(". "*(n-i)+"0 "+". "*(n-i))
    else:
        dots = ". " *(n-i)
        print(dots+"0 "*((((i-1)*2)-1)+2)+dots)

for j in range(n-1,0,-1):
    if j == 1:
        print(". "*(n-j)+"0 "+". "*(n-j))
    else:
        dots =". " * (n-j)
        print(dots+"0 "*((((j-1)*2)-1)+2)+dots)