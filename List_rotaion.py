def converting_int(numbers):
    num_list = []
    for i in numbers:
        i = int(i)
        num_list.append(i)
    return num_list

def rotation(number,no_of_rotation):
    rotaion_time = no_of_rotation % (len(number))
    first_part = number[:rotaion_time]
    second_part = number[rotaion_time:]
    return  second_part + first_part

numbers = input().split(",")
no_of_rotation = int(input())
number = converting_int(numbers)
new_list = rotation(number,no_of_rotation)
print(new_list)