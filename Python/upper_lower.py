def upper_lower(word):
    upper_l = ""
    lower_l = ""
    for i in word:
        if i.isupper():
            upper_l += i
        else:
            lower_l += i
    return (upper_l+"\n"+lower_l)

word = input()
print(upper_lower(word))