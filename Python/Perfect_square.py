m = int(input())
n = int(input())

perfect_square = False
for i in range(m,n+1):
    if int(i ** 0.5) ** 2 == i:
        perfect_square = True
        print(i)
        break
if not perfect_square:
    print("No Perfect Square")