def converting_int(num_list):
    num_int_list = []
    for i in num_list:
        i = int(i)
        num_int_list.append(i)
    return num_int_list

num_list = input().split()

num_int_list = converting_int(num_list)
print(num_int_list)

l = len(num_int_list)

max_sum = float('-inf')

for i in range(l):
    current_sum = 0
    for j in range(i,l):
        current_sum += num_int_list[j]
        max_sum = max(max_sum,current_sum)

print(max_sum)