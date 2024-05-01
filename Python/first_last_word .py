# gives input in one line using space 
s = input()

p = s.split()

for i in p:
    l = len(i)
    i = i.lower()
    for j in range(l):
        if i[0] == i[l-1]:
            print(True)
            break
        else:
            print(False)
            break