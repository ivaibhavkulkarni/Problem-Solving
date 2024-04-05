def consecutive_sum(num):
    con_sum_list = []
    stop_index = len(num) - 1
    for i in range(stop_index):
        value = num[i] + num[i+1]
        con_sum_list.append(value)
    return con_sum_list

def printing_consecutive_num(num):
    while len(num) > 1:    
        consecutive = consecutive_sum(num)
        print(consecutive)
        num = consecutive
        
def converting_int(num_list):
    num = []
    for i in num_list:
        i = int(i)
        num.append(i)
    return num

num_list = input().split(",")
num = converting_int(num_list)
print(num)
printing_consecutive_num(num)
