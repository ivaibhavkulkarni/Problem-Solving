final_1 = {}
final_2 = {}
keys_1 = input().split()
values_1 = input().split()

keys_2 = input().split()
values_2 = input().split()

l_1 = len(keys_1)
l_2 = len(keys_2)

for i in range(l_1):
    final_1[keys_1[i]] = int(values_1[i])
    
for j in range(l_2):
    final_2[keys_2[j]] = int(values_2[j])

final_1.update(final_2)
final_1 = sorted(final_1.items())
print(final_1)



