def printing_anti_diagonal(new_list,m,n):
    for k in range(m+n-1):
        for i in range(m):
            for j in range(n):
                if i + j == k:
                    print(new_list[i][j],end = " ")
        print()
def converting_int(matrix):
    num_list = []
    for i in matrix:
        i = int(i)
        num_list.append(i)
    return num_list


num = input().split()
m = int(num[0])
n = int(num[1]) 

new_list = []
for i in range(m):
    matrix = input().split()
    num_list = converting_int(matrix)
    new_list.append(num_list)
final = printing_anti_diagonal(new_list,m,n)
