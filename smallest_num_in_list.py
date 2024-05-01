def cahr_int(i):
    i = int(i)
    return i 

list_input = input().split()
map_num_list = map(cahr_int,list_input)
list_num = list(map_num_list)
list_num.sort()
smallest_missing = 1

for num in list_num:
    if num == smallest_missing:
        smallest_missing += 1
print(smallest_missing)