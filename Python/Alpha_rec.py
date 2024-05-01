string = ['A','B','C','D','E','F','G','H','I','J','K'
          ,'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

m = int(input())
n = int(input())
a = 0
for i in range(m):
    final = ""
    for j in range(n):
        if i == 0 or i == m-1:
            final = final + string[a] + " "
            a+=1
        else:
            if j == 0 or j == n-1:
                final += string[a] + " "
                a+=1
            else:
                final+="  "
                a+=1
    print(final)