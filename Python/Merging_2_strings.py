string_1 = input()
string_2 = input()
max_len = max(len(string_1),len(string_2))
len1 = len(string_1)
len2 = len(string_2)
final_string = ''
for i in range(max_len):
    if i < len1:
        final_string += string_1[i]
    if i < len2:
        final_string += string_2[i]

print(final_string)