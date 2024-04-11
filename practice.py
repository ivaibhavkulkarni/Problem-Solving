n = 3
flat_list = [1, 2, 3, 5, 10, 11, 15, 20, 30]

nested = []
for item in range(0,len(flat_list),n):
    row = flat_list[item:item+n]
    nested.append(row)
print(nested)

for i in nested:
    row = ""
    for item in i:
        row+= str(item) + " "
    print(row)