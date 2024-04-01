def sum_of_unique_pairs(numbers,n):
    num_list = []
    for i in numbers:
        i = int(i)
        num_list.append(i)
    stop_index = len(num_list) - 1
    unique_pair_set = set()
    for current_index in range(stop_index):
        num1 = num_list[current_index]
        num2 = n - num1
        remaining_list = num_list[current_index + 1:]
        if num2 in remaining_list:
            pair = (num1,num2)
            pair = tuple(sorted(pair))
            unique_pair_set.add(pair)
    return unique_pair_set


numbers = input().split()
n = int(input())
values = sum_of_unique_pairs(numbers,n)

print(sorted(values))