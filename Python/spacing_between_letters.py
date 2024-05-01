a = input()
b = ""
l = len(a)

for index, i in enumerate(a):
    if i == i.upper() and index != 0:
        b = b +" "+i
    else:
        b += i
print(b)