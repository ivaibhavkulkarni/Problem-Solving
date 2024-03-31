# in a given list odd number of repeated number should be print

n = input().split()
int_list = []

for i in n:
    int_list.append(int(i))

final = []
for j in int_list:
    if int_list.count(j) % 2 != 0 and j not in final:
        final.append(j)

final.sort()
print(final)
