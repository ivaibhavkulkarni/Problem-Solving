n = int(input())

for i in range(1,n+1):
    final = ""
    a = 1
    for j in range(1,i+1):
        if i == 1 or i == 2 or i == n:
            left_spaces = "  " * (n-i)
            final = str(a) +" "+ final
            a+=1
        else:
            if i > 2 or i < n-2:
                hollow = " " *(i-3+j)
                left_spaces = " "*(n-i)
                final = left_spaces + str(i) + hollow + "1"
            
        
    print(left_spaces+final)