L = ["vaibhav","ferrari","aston martin",9,2,5,9.00,10.00]

m = int(input())
n = int(input())
l = len(L)
new_list = []
c = L[m]
L[m] = L[n]
L[n] = c
for i in range(l):
    new_list += [i]
print(L)

# L = ["vaibhav","ferrari","aston martin",9,2,5,9.00,10.00]
#            0      1           2         3 4 5   6    7


