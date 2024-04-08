words = input().split()
n = int(input())


new_list = []
for i in range(len(words)):
    if len(words[i]) != n:
        new_list.append(words[i])
print(" ".join(new_list))