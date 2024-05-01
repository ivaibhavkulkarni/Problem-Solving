m = int(input())
n = int(input())

for i in range(m, 0, -1):
    final = ""
    a = n
    for j in range(1, i + 1):
        if j == 1 or j == i or i == m:
            final += str(a) + " "
        else:
            final += "  "
        a += 1
    spaces = " " * (m - i)
    print(spaces + final)