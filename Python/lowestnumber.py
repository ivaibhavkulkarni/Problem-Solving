n = int(input())

small = 9999999

for i in range(n):
    m = int(input())
    if m < small:
        small = m
    print(small)