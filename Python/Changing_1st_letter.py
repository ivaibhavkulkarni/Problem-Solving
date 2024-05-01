string = input() 
string = string.split() 
length_of_string = len(string)
result ="" 
for i in string: 
    if length_of_string > 0: 
        new_word = chr(ord(i[0]) + 1) +i[1:]  
        result += new_word + " "  
print(result)