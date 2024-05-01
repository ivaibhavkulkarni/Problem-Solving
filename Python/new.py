"""w = "python"

for x in w:
    print(x)"""


""""for number in range(0,10):
    print(number)"""


"""for i in range(1,5):
    print("* "*i)"""

""""n = int(input())

for i in range (1,n-1):
    print(i)"""

"""a = (input())
c = len(a)
b = ""

for i in range (0,c):
    b += a[i] + "-" 
    
print(b)"""

""""f = 5
for i in range(1,5):
    f = f * i
print(f)"""


"""x = 10
for i in str(x):
    print(i)"""

"""a = 10
b = 20
t= 0

for i in range(4):
    print(i)"""

"""a = "christopher"
b = ""

for x in a[6:]:
    b = b + x
print(b)"""

"""n = 89456
r = ""

for i in str(89456):
    r = i + r
print(r)"""


"""n = int(input())
n = str(n)
l = len(a)

for i in range(0,l):
    print(n[i],end=" ")"""


"""n = 5

for i in range(n,0,-1):
    print(i)"""


""""n = int(input())

n = str(n)
l = len(n)
print(l)
sum = 0

for i in range(0,l):
    sum = (int(n[i]))**l + sum
print(sum)

if sum == int(n):
    print("Amstrong")
else:
    print("NON")"""



# greatest

"""n = int(input())

f_n = int(input())
g_n = int(input())

for i in range(n-1):
    num = int(input())
    if num > g_n:
        g_n = num
print(g_n)"""

# no of number from m-n

"""m = int(input())
n = int(input())
count = 0

for i in range(m,n+1):
    l_n = len(str(i))
    count = count + l_n
print(count)"""


# given n is divisible by num from 2-9 :

"""
n = int(input())

for i in range(2,10):
    if n % i == 0:
        is_divisible = True

if is_divisible:
    print("Divisible")
else:
    print("Not Divisible")"""

# alternate number should be minus and print the sum of series 
# x**2 + -x**4 

"""num = int(input())
n = int(input())
power = 2
sum = 0

for i in range(1,n+1):
    new = num ** power
    power += 2
    if i % 2 ==0:
        new *= -1
    
    sum = sum + new
print(sum)"""




#P7