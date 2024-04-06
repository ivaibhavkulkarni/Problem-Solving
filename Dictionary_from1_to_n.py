final = {}
n = int(input())

for i in range(1,n+1):
    key , value = i , i ** 2
    final[key] = value
print(final) 