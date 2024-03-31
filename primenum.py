n = int(input())
factors = 0
for i in range(2,n):
    if n%i ==0:
        factors += 1
if factors == 0:
    print("Prime number")
else:
    print("Not a prime number")
        


 