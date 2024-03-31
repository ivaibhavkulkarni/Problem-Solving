def fibonacci_series(n):
    if n <=1:
        return n
    return fibonacci_series(n-1) + fibonacci_series(n-2)


def get_fibonacci_series(n):
    
    m = []
    for i in range(n):
        term = fibonacci_series(i)
        m.append(term)
    return (m)



n = int(input())

print(get_fibonacci_series(n))