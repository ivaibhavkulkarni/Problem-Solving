m = int(input())
n = int(input())
number = 1
for i in range(m):
    final = ""
    for j in range(n):
        final = final + str(number) + " "
        number = int(number) + 1
    print(final)