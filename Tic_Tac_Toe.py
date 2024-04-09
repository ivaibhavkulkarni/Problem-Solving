def Tic_Tac_Toe(matrix):

    # checking for row 
    for i in range(m):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            return matrix[i][0]
    
    # checking for colomn

    for i in range(m):
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:
            return matrix[0][i]
        
    # checking for diagonal

    for i in range(m):
        if matrix[0][0] == matrix[1][1] == matrix[2][2]:
            return matrix[0][0]
        elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
            return matrix[0][2]
    
    # checking Tie

    for i in range(m):
        for j in range(m):
            if matrix[i][j] != "O" or matrix[i][j] != "X":
                return None 
    return "Tie"

m = 3
n = 3

matrix = []

for i in range(m):
    input_list = input().split()
    matrix.append(input_list)
final = Tic_Tac_Toe(matrix)

if final == "O":
    print("Abhinav Wins")
elif final == "X":
    print("Anjali wins")
else:
    print("Tie")


