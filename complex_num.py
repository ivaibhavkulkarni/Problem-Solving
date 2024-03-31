n = int(input())

a = 0
for x in range(1,n+1):
    for y in range(1,x+1):
        a+=1
start_number = a


for i in range(n, 0, -1):
    final = ""
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            final += str(start_number) + " "
            start_number -= 1
        else:
            final += "   "
            start_number-=1
    print(final)