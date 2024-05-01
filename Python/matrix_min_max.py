def converting_int(num):
    num_list = []
    for i in num:
        i = int(i)
        num_list.append(i)
    return num_list

m , n = input().split()
m , n = int(m),int(n)

num_list = []
for i in range(m):
    num = input().split()
    num_int = converting_int(num)
    num_list.append(num_int)

print(num_list)

row_max = []
row_min = []
row_sum = []

for row in num_list:
    row_max.append(max(row))
    row_min.append(min(row))
    row_sum.append(sum(row))
print(max(row_max))
print(min(row_min))
print(sum(row_sum))
