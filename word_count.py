words = input().split()
sorted_words = sorted(words)

final = {}
for i in sorted_words:
    count = words.count(i)
    final[i] = count

for j in final:    
    mes = "{}: {}"
    print(mes.format(j,final[j]))
