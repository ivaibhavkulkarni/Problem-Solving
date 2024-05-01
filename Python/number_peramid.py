n = int(input())

num = 1
for i in range(1,n+1):
    final = ""
    for j in range(1,i+1):
        final = final + str(num) + " "
        num = num + 1
    print(final)