def multiply(n):
    if n == 1:
        return 1
    return n * multiply(n-1)

num = int(input())
print(multiply(num))

# 5* 4 * 3 * 2 * 1 

# the way runs is line 2 is the base case where recursive function stops
# 1 * 2  * 3 * 4 * 5 and return multiple 120