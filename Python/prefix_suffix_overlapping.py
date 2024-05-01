a = input()
b = input()

answer = ""
for i in range(len(a)):
    for j in range(len(b)):
        if a[i:] == b[:j]:
            if len(a[i:]) > len(answer):
                answer = a[i:]

if answer == "":
    print("No overlapping")
else:
    print(answer)