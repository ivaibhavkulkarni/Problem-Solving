def converting_int(num_list):
    num_list_int = []
    for i in num_list:
        i = int(i)
        num_list_int.append(i)
    return num_list_int

num_list = input().split()
num_list_int = converting_int(num_list)
length = len(num_list_int)

for i in range(length):
    current_sum = 0
    for j in range(i,length):
        