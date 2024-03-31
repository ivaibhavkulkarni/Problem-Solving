n = input().split(",")
int_list = []
for i in n:
    int_list.append(int(i))

largest_num = 0
mode = 0

for j in int_list:
    each_num = int_list.count(j)
    if each_num > largest_num:
        largest_num = each_num
        mode = j
print(mode)