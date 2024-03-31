n = int(input())

for i in range(1,n+1):
    left = ". " * (n-i)
    middle = "0 " *(2 * i -1)
    right = ". " *(n-i)
    print(left+middle+right)