def converting_int(matrix_input):
    num_list = []
    for i in matrix_input:
        i = int(i)
        num_list.append(i)
    return num_list

num = input().split()
m = int(num[0])
n = int(num[1])


for i in range(m):
    matrix_input = input().split()
    converting_int(matrix_input) 