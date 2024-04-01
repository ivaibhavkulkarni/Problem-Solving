def converting_int(numbers):
    num_list = []
    for n in numbers:
        i = int(n)
        num_list.append(i)
    return num_list

def sum_of_n_unique_values(number,n):
    stop_index = len(number)-1
    final_pair = []
    for current_index in range(stop_index):
        num1 = number[current_index]
        num2 = n - num1
        remaining_list = number[current_index + 1:]
        if num2 in remaining_list:
            pair = (num1,num2)
            final_pair.append(pair)
    return final_pair

numbers = input().split()
n = int(input())
number = converting_int(numbers)
values = sum_of_n_unique_values(number,n)
for value in values:    
    print(value)