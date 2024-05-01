n = int(input())
 
for a in range(1,n+1):
    final = ""
    for b in range(1,a+1):
        final = final + str(b) + " "
        spaces = " " * (n-b)
        part1 = (spaces+final)
    print(part1)
for i in range(n-1,0,-1):
    final = ""
    for j in range(1,i+1):
        final = final + str(j) + " "
        spaces = " " * (n-j)
        part2 = (spaces+final)
    print(part2)