#common factors

m = int(input())
n = int(input())

if m > n:
    small = n
else:
    small = m

gcd = small

for i in range(1,small+1):
    if m % i == 0 and  n % i == 0:
        gcd = i

print(gcd)