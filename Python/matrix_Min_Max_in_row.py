def min_max_sum(num_list):
    final = []
    max_list = []
    min_list = []
    sum_list = []
    for i in num_list:
        max_list.append(max(i))
        min_list.append(min(i))
        sum_list.append(sum(i))
    final.append(max_list)
    final.append(min_list)
    final.append(sum_list)
    return final

def converting_int(num_list):
    matix = []
    for i in num_list:
        i = int(i)
        matix.append(i)
    return matix


m , n = input().split()
m , n = int(m),int(n)

num = []
for i in range(3):
    num_list = input().split()
    matrix = converting_int(num_list)
    num.append(matrix)

final = min_max_sum(num)
for i in final:
    print(i)