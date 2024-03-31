n = int(input())

for i in range(1, n + 1):
    left_zeros = "0 " * (n - i)
    middle_ones = "1 " * (2 * i - 1)
    right_zeros = "0 " * (n - i)
    print(left_zeros + middle_ones + right_zeros)
