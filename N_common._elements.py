def converting_int(num_list):
    num_int_list = []
    for i in num_list:
        i = int(i)
        num_int_list.append(i)
    return num_int_list

def common_element(no_num_list):
    result = no_num_list[0]
    for num_list in no_num_list:
        result = result.intersection(num_list)
    return result


n = int(input())
no_num_list = []
for i in range(n):
    num_list = input().split()
    new_num_list = converting_int(num_list)
    set_num = set(new_num_list)
    no_num_list.append(set_num)

final = common_element(no_num_list)
final = list(final)
final.sort()
print(final) 