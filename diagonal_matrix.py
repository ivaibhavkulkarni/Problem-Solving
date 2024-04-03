def printing_diagonal_matrix(num_list,m,n):
    final = []
    for i in range(m):
        final.append(num_list[i][i])
    return final
def converting_int(num_list):
    final = []
    for i in num_list:
        i = int(i)
        final.append(i)
    return final

m , n = input().split()
m , n = int(m), int(n)

num_list_f = []
for i in range(m):
    num_list = input().split()
    matrix = converting_int(num_list)
    num_list_f.append(matrix)

final = printing_diagonal_matrix(num_list_f,m,n)
print(final)