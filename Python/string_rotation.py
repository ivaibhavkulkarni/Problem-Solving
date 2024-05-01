a = input()
n = int(input()) % len(a)
second_part = a[n:]
first_part = a[:n]

print(second_part+first_part)
