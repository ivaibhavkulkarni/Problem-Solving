n = int(input())

for i in range(1,n+1):
    final = ""
    for j in range(1,n+1):
        if i == 1 or i == n:
            final = final + str(j) + " "
        else:
            if j == 1 or j == n:
                final = final + str(j) + " "
            else:
                final = final + "  "
    print(final)
