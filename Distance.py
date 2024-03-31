# 0 - 40 km (*2 points)
# 41 - 60 km (*4 points)
# 61 - 120 km (*6 points)
# 120 km > (*8 points)
# adding 50 as bonus

n = int(input())

if n > 0 and n <= 40:
    print((n * 2)+50)

elif n >= 41 and n <=60:
    num = n - 20
    print( 80 + (num * 4) + 50)

elif n > 60 and n <= 120:
    num = n - 60
    print( 80 + 80 + (num * 6) + 50)

elif n > 120:
    num = n - 120
    print(80 + 80 + 360 +(num * 8 ) + 50 ) 