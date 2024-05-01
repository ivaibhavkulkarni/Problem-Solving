n = int(input())

num = []
for i in range(n):
    m = int(input())
    num.append(str(m))
print(num)

for j in range(n):
    count = 0
    for k in range(1,int(num[j])+1):
        if int(num[j]) % k == 0:
            count +=1
    if count == 2:
        break
print(num[j])