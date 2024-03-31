def check_prime(m,n):
    
    final = ""
    for i in range(m,n+1):
        is_prime = True
        for j in range(2,int(i ** 0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime and i > 1:
            final += str(i) + " "

    return final



m = int(input())
n = int(input())
prime = check_prime(m,n)
print(prime)