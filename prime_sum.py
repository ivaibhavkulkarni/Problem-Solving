n = int(input("Enter the number of values to check: "))

f_sum = 0
for i in range(n):
    F_num = int(input("Enter a number: "))
    if F_num == 1:  # Skip 1
        continue
    is_prime = True
    for a in range(2, int(F_num**0.5) + 1):
        if F_num % a == 0:
            is_prime = False
            break
    if is_prime:
        f_sum += F_num

print("Sum of prime numbers (excluding 1):", f_sum)
