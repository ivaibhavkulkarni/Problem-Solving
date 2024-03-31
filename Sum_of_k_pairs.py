def get_unique_pairs(int_list,pair_sum):
    stop_index = len(int_list) - 1
    unique_pair_set = set()
    for current_index in range(stop_index):
        num1 = int_list[current_index]
        num2 = pair_sum - num1
        remaining_list = int_list[current_index + 1:] 
        if num2 in remaining_list:
            pair = (num1,num2)
            pair = tuple(sorted(pair))
            unique_pair_set.add((pair))
    return unique_pair_set


def converting_int(num_list):
    new_num_list = []
    for i in num_list:
        i = int(i)
        new_num_list.append(i)
    return new_num_list

num_list = input().split(",")
pair_sum = int(input())

int_list = converting_int(num_list)
unique_values = get_unique_pairs(int_list,pair_sum)
for pair in unique_values:
    print(pair)