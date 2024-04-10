def flat_lsit(num_l):
    flatlist = []

    for element in num_l:
        if type(element) is list:
            for item in element:
                flatlist.append(item)
        else:
            flatlist.append(element)
    return flatlist

num = input().split()
m = int(num[0])
n = int(num[1])

num_l = []
for i in range(m):
    num_list = input().split()
    num_l.append(num_list)
print(num_l)

final = flat_lsit(num_l)
print(final)