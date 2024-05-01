final = {}

keys = input().split(",")
values = input().split(",")
l = len(keys)

for i in range(l):
    final[keys[i]] = values[i]

sorted_final = sorted(final.items())

for j in sorted_final:
    print(j[0],j[1])