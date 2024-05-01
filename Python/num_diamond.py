n = int(input())
#upper part
for i in range(1,n+1):
    final = ""
    for j in range(1,i+1):
        if i == 1:
            left_space = " " * ((n-i))
            final = final + str(1) + " "
        else:
            left_space = " " * ((n-i))
            hollow = "  " * (i-2)
            final = str(1) + " " 
            final = final + hollow + str(j)
        upper_part=(left_space+final)
    print(upper_part)
#bootom_part
for a in range(n-1,0,-1):
    final = ""
    l_space = " " * ((n-a))
    for j in range(1,a+1):
        if a == 1:
            final = final + str(1) + " "
        else:
            hollow = "  " * (a-2)
            final = str(1)+" "
            final = final +hollow +str(j)
        bottom_part=(l_space+final)
    print(bottom_part)    

