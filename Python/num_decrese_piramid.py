n = 4
x = 2
for a in range(1,n+1):
    for b in range(1,a+1):
        x+=1
start_num = x-1



for i in range(n):
    final = ""
    
    final += " " * (i * 2)
    
    for j in range(n - i):
        if i == 0 or j == 0 or j == (n - i - 1):
            final += str(start_num) + " "
        else:
            final += "  "  
        start_num -= 1
        
    print(final)
