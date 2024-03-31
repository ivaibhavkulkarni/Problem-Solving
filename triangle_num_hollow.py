n = int(input())


for i in range(1,n+1):
    final = ""
    a = 5
    for j in range(1,i+1):
        if i == 1 or i == 2 or i == n:
            left_spaces = " " * (n-i)
            final = final + str(a) + " "
            a+=1
        else:
            a = 5                   #here in else block also initialize a as 5
            left_spaces = " " * ( n-i)
            final = str(a) + " "                #here only concate a
            hollow_space = "  "*(i-2)          #calculate hollow_space also
            a+=(i-1)                        #increment a by i-1
            final = final + hollow_space + str(a)          #here concate hollow_space and a with final
            a+=1
    print(left_spaces+ final)