a = "TilteCase"
l = len(a)
first_letter = a[0].lower()
n = ""
for i in range(1,l):
    if a[i].isupper():
        n += "-" + a[i]
    else:
        n += a[i]
print(first_letter+n.lower())