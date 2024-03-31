# Write a program that reads Distance km and calculates the score
# 0 -50km for each km its 3 score and 
# 51 - 100 km 5 score 
# 101 - 200 km 6 score
# 200 > 10 score 


n = int(input())

if n >= 0 and n <= 50:
    result = (n * 3) + 100
    print(result)
elif n >= 51 and n <= 100:
    result = 150 + ((n-50) * 5) + 100
    print(result)
elif n >= 101 and n <= 200:
    result = 150 + 250 + ((n -100)* 6) + 100
    print(result)
elif n > 200:
    result = 150 + 250 + 600 + ((n - 200)*10 ) + 100
    print(result)