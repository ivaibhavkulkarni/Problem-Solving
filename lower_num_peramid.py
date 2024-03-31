n = int(input())

for i in range(n,0,-1):
    final = ""
    a = 1 
    for j in range(1,i+1):
        if i == n or i == 2 or i ==1 :
            space = " " * (n-i)
            final = final + str(a) + " "
            a +=1
        else:
            if i < n or i >2:
                space = " " * (n-i)
                hollow = "  " * (i-2)
                final = "1 " + hollow +str(a)+" "
            a+=1
    print(space+final)