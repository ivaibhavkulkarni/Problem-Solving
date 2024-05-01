num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]
n = int(input())
new_list = []
for tuple_a in num_list:
    if n in tuple_a:
        new_tuple = tuple_a[:tuple_a.index(n)] + tuple_a[tuple_a.index(n)+1:]
        new_list.append(new_tuple)
    else:
        new_list.append(tuple_a)

print(new_list)