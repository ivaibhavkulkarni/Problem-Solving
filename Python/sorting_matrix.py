def converting_flat_list_to_nested(flat_list):
    nested_list = []
    for i in range(0, len(flat_list), n):
        row = flat_list[i:i+n]
        nested_list.append(row)
    return nested_list

##########################################

def converting_nested_into_flat(num_nested):
    flatlist = []
    for element in num_nested:
        if type(element) is list:
            for item in element:
                flatlist.append(item)
        else:
            flatlist.append(element)
    return flatlist

#############################################

def converting_int(num_input):
    new_num_list = []
    for i in (num_input):
        i = int(i)
        new_num_list.append(i)
    return new_num_list

#################################################

num = input().split()
m = int(num[0])
n = int(num[1])

num_nested = []
for i in range(m):
    num_input = input().split()
    num_int_list = converting_int(num_input)
    num_nested.append(num_int_list)
print(num_nested)

flat_list = converting_nested_into_flat(num_nested)
flat_list.sort()
sorted_flat_list = flat_list 
final = converting_flat_list_to_nested(sorted_flat_list)

for element in final:
    row = ''
    for item in element:
        row += str(item) + " "
    print(row) 