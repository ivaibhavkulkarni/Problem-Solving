n = int(input())

#top
for i in range(1,n+1):
    #left_part
    upper_part_l = "* " *(i)
    #Right_part
    spaces = "  " *(2*(n-i))
    right_part = "* " * (i)
    print(upper_part_l+spaces+right_part)

#bottom

for j in range(n,0,-1):
    #botom_left
    bottom_left_part = "* " * (j)
    #bottom_right
    spaces = "  " * (2*(n-j))
    bottom_right = "* " * (j)
    print(bottom_left_part+ spaces + bottom_right)