def get_reversed_String(string):

    if len(string) == 1:
        return string[0]
    else:
        return string[len(string)-1] + get_reversed_String(string[:-1])

string = input()
print(get_reversed_String(string))