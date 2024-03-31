#The favorite dish of all ages was apple pie
n = input().split()
final = []
for i in n:
    if i[0] == "a":
        if i in final:
            final.remove(i)
    else:
        final.append(i)
    
print(final)