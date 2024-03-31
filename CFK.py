n = input()

number = ""
C = 0
F = 0
K = 0
for j in n:
    if j.isalpha():
        break
    number+=j

number = (number)

for i in n:
    if i == "C":
        print(number)
        F = round((number)*(9/5) + 32,2)
        K = round(number + float(273),2)
        print(str(F)+"F")
        print(str(K)+"K")
    elif i == "F":
        C = round((number-float(32))*(5/9),2)
        print(str(C)+"C")
        print(number)
        K = round(C + float(273),2)
        print(str(K)+"K")
    elif i == "K":
        C = round(number - float(273),2)
        print(str(C)+"C")
        F = round((C * (9/5)) + 32,2)
        print(str(F)+"F")
        print(number)

