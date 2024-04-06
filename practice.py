def printing_consecutive_num(num_list):
    consecutive_list = []
    stop_index = len(num_list) - 1
    for i in range(stop_index):
        sum_value = num_list[i] + num_list[i+1]
        consecutive_list.append(sum_value)
    return consecutive_list

def converting_int(num):
    num_list = []
    for i in num:
        i = int(i)
        num_list.append(i)
    return num_list
num = input().split(",")
num_list = converting_int(num)
print(num_list)

while len(num_list) > 1:    
    final = printing_consecutive_num(num_list)
    print(final)
    num_list = printing_consecutive_num(num_list)
