#given two number m and k write a program to print the kth largest factor 
#of given numbr n

m = int(input())
k = int(input())

factors = []
for i in range(1, m+1):
    if m % i == 0:
        factors.append(i)

if k <= len(factors):
    print(factors[-k])
else:
    print("Invalid value of k")