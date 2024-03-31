a = input()
contains_upper = False
contains_lower = False
contains_digit = False


for i in a:
    if i.isupper():
        contains_upper = True
    elif i.islower():
        contains_lower = True
    elif i.isdigit(): 
        contains_digit = True

if contains_digit and contains_lower and contains_upper:
    print("valid password")
else:
    print("Invalid password")
