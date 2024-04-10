def no_of_rotations(a,b):
    if len(a) != len(b) or a != b:
        return "No Match"
    else:
        len_a = len(a)
        for i in range(len_a):
            i = i * (-1)
            second_part = a[i:]
            first_part = a[:i]
            final = second_part + first_part
            if final == b:
                return i * (-1)
    return "No Match"
a = input()
b = input()

final = no_of_rotations(a,b)

print(final)