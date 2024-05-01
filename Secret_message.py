lower_string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z']
message_input = input().lower()
number = ""

for i in message_input:
    if i == " ":
        number = number[:-1] + "  "
    else:
        index_num = str(lower_string.index(i) + 1)
        number += index_num + "-"
print(number[:-1]) 
