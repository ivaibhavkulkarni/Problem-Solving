n = int(input())
final=0
for i in range(1,n+1):
    if n % i == 0:
        if i < n:
            final = i
print(final)