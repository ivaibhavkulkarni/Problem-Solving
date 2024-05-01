#P1
#o/p
"""
*
* *
* * *
* * * *

n = int(input())

for i in range(1,n+1):
    print("* "*i)"""

#P2
#O/p

"""      
      *
    * *
  * * *
* * * *

n = int(input())

for i in range(1,n+1):
    space = "  "*(n-i) 
    star = "* " * i
    print(space + star)"""

#P3
#O/P

"""     
     *
    ***
   *****
  *******
  

n = int(input())

for i in range(1,n+1):
    spaces = "  "*(n-i)
    star = "* " *((2*i) -1)
    print(spaces+star)

"""

#P4
#O/P


"""        
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5

#number piramid
 
n = int(input())

for i in range(1,n+1):
    spaces = "  "*(n-i)
    i = str(i)
    num = (i + " ")*((2*int(i))-1)
    print(spaces + num)"""

#opposite to above pro

"""n = int(input())

for i in range(n,0,-1):
    spaces = "  "* (n-i)
    i = str(i)
    num = (i + " ")*((2*int(i))-1)
    print(spaces + num)"""


#P5
# printing M with star
#O/P

"""
    *                 *
    * *             * *
    * * *         * * *
    * * * *     * * * *
    * * * * * * * * * *


n = int(input())

for i in range(1,n+1):
    one_half = "* " * i

    spaces = "    " * (n-i)
    stars = "* " *(i)
    second_half = spaces + stars
    print(one_half+second_half)"""

#P6
# O/P

"""
  *
  * *
  * * *
  * *
  *


n = int(input())

for i in range(1,n):
    one_half = "* " *i
    print(one_half)
for j in range(n,0,-1):
    second = "* " * j
    print(second)"""


#P7
#O/P
"""
+ + + + + + + + +
  + + + + + + +
    + + + + +
      + + +
        +

n = int(input())

for i in range(n,0,-1):
    spaces = "  " *(n-i)
    stars = "+ " * ((2*i)-1)
    top = spaces + stars
    print(top) """

#P8
#O/P


""""
        #
      + #
    + + #
  + + + #
+ + + + #
  + + + #
    + + #
      + #
        #

n = int(input())

for i in range(1,n):
    spaces = "  "*(n-i)
    stars = "+ " * (i-1) + "# "
    top = spaces + stars 
    print(top)

for j in range(n,0,-1):
    spaces = "  " * (n-j)
    stars = "+ " * (j-1) + "# "
    bottom = spaces + stars
    print(bottom)"""


#P9
#O/P

"""
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *

n = int(input())

for i in range(1,n):
    spaces = "  " * (n-i)
    star = "* " * (i)
    t_l = star + spaces
    t_r = spaces + star
    top = (t_l + t_r)
    print(top)

for j in range(n,0,-1):
    spaces =  "  " * (n-j)
    star = "* " * (j)
    b_l = star + spaces
    b_r = spaces + star
    bottom = b_l + b_r
    print(bottom)"""

#P10
#O/P

"""
    *
   * *
  * * *
 * * * *
* * * * *

n = int(input())

for i in range(1,n+1):
    spaces = " " *(n-i)
    stars = "* " * i
    print(spaces + stars)"""


#P11
#O/P
"""
+ + + + +
 * * * *
  * * *
   * *
    *
n = int(input())

for i in range(n,n-1,-1):
    plus = "+ " * i
    print(plus)
  
for i in range(n-1,0,-1):
    spaces = " " * (n-i)
    stars = "* " * i
    print(spaces+stars)"""

#P12
#O/P
"""
* * * * * * * * *
 * * * * * * * *
  * * *   * * *
   * *     * *
    *       *

num_rows = 5
print("* " * (2 * num_rows - 1))

for i in range(1, num_rows):
    left_spaces = " " * (i)
    stars = "* " * (num_rows - i)
    middle_spaces = "  " * (i - 1)           
    print(left_spaces + stars + middle_spaces +stars)"""

#P13
#O/P
"""
          *
        * * 
      *   * 
    *     *
  *       *
* * * * * *

n = int(input())

for i in range(0,n):
    if i == 0:
        print("  "*(n-1) + "*")
    elif i == n-1:
        print("* "*n)
    else:
        left_space = "  " * ((n-i)-1)
        hallow_space = "  " * (i-1)
        print(left_space + "* " + hallow_space + "* ")"""

#P14
#O/P
"""
* * * * * 
* 0 0 0 * 
* 0 0 0 * 
* 0 0 0 * 
* * * * *

n = int(input())

for i in range(0,n):
    if i == 0:
        print("* "*n)
    elif i == (n-1):
        print("* "*n)
    else:
        zeros = "0 " * (n-2)
        print("* "+ zeros+ "* ")"""


#P15
#O/P
"""
* * * * * * * *
* 0 0 0 0 0 0 *
* 0 0 0 0 0 0 *
* * * * * * * *

m = int(input())
n = int(input())

for i in range(0,m):
    if i == 0 :
        print("* "*n)
    elif i == (m-1):
        print("* "*(n))

    else:
        zeros = "0 "* (n-2)
        print("* "+ zeros + "* ")
"""

#P16
#O/P
"""
.
. .
. 0 .
. 0 0 .
. 0 0 0 .
. 0 0 0 0 .
. . . . . . .

n = int(input())

for i in range(0,n):
    if i == 0:
        print(". "+" "*(n-1))
    elif i == (n-1):
        print(". "*n)
    else:
        zeros = "0 "*(i-1)
        print(". "+zeros+". ")"""

#P17
#O/P

"""
_______
|     /
|    /
|   /
|  /
| /
|/
n = int(input())

for i in range(0,n+1):
    if i == 0:
        print("_"*(n+1))
    else:
        spaces = " " * (n-i)
        print("|"+spaces+"/")"""


#P18
#O/P


"""
    *
   * *
  *   *
 *     *
* * * * *


n = int(input())

for i in range(0,n):
    if i == 0:
        h = int(((n*2)-1)/2)
        print(" "*h+"* "+" "*h)
    elif i == n-1:
        print("* "*n)
    else:
        left_spaces = " "*((n-i)-1)
        hollow_spaces = "  "*(i-1)
        print(left_spaces+"* "+hollow_spaces+"* ")"""


#P19
#O/P
"""
# # # # #
+     +
+   +
+ +
+
n = int(input())

for i in range(0,n):
    if i == 0:
        print("# "*n)
    elif i == n-1:
        print("+ ")
    else:
        H_spaces = " "* ((n-i-2)*2)
        print("+ "+H_spaces+"+ ")"""

#P20
#O/P
"""
1
2 2
3   3
4     4
5       5
4     4
3   3
2 2
1


n = int(input())


for i in range(0,n):
    if i == 0:
        print(i+1)
    else:
        spaces = " "*((i-1)*2)
        i = i + 1
        i = str(i) + " "
        print(i+spaces+i)

for j in range(n-1,0,-1):
    if j == 1:
        print(1)
    else:
        spaces = " "*((j-2)*2)
        j = str(j) + " "
        print(j+spaces+j)"""


#P21
#O/P
"""
        *
      * *
    *   *
  *     *
* * * * *


n = int(input())

for i in range(0,n):
    if i == 0 :
        print(" "*((n*2)-2) +"* ")
    elif i == n-1:
        print("* "*n)
    else:
        left_spaces = " "*((n-i-1)*2)
        hollow_spaces = "  "*(i-1)
        print(left_spaces+"* "+hollow_spaces+"* ")"""

#P22
#O/P
"""
* * * * *
 *     *
  *   *
   * *
    *


n = int(input())

for i in range(0,n):
    if i == 0:
        print("* "*n)
    elif i == n-1:
        print(" "*(n-1)+"* "+" "*(n-2))
    else:
        left_space = " "*i
        hollow_space = " "*((n-2-i)*2)
        print(left_space+"* "+hollow_space+"* ")"""

#P23
#O/P
"""
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *


n = int(input())

for i in range(0, n):
    if i == 0:
        h = int(((n * 2) - 1) / 2)
        print(" " * h + "* " + " " * h)
    else:
        spaces = " " * ((n - i - 1))
        hollow = " " * ((i - 1) * 2)
        print(spaces + "* " + hollow + "* ")

for j in range(n - 1, 0, -1):
    if j == 1:
        h = int(((n * 2) - 1) / 2)
        print(" " * h + "* " + " " * h)
    else:
        spaces = " " * ((n - j + 1)-1)
        hollow = " " * ((j - 2)) * 2
        print(spaces + "* " + hollow + "* ")
"""

#P24
#O/P
"""
        1 
      2 2 
    3   3
  4     4
5       5
  4     4
    3   3
      2 2
        1


n = int(input())

for i in range(1,n+1):
    if i == 1:
        left_spaces = " "*((n-i)*2)
        print(left_spaces + str(i) )
    
    else:
        left_spaces =" "*((n-i)*2)
        hollow = " "*(2*i-3)
        number = str(i) 
        print(left_spaces+number+hollow+number)
        k = n-1
for i in range(1,n):
    if i == n - 1:
        left_spaces = " " * ((i)*2)
        print(left_spaces+str(1))

    else:
        left_spaces = " " * ((i)*2)
        hollow = " "*(2 * k - 3)
        number = str(k)
        print(left_spaces + number + hollow + number)
        k = k -1"""


#P25
#O/P
"""
+ + + +
  *   *
    * *
      *


n = int(input())

for i in range(0,n):
    if i == 0:
        print("+ "*n)
    elif i == n-1:
        print("  "*(n-1)+"* ")
    else:
        left_spaces = "  " * (i)
        hollow = "  "*(n-i-2)
        print(left_spaces+"* "+hollow+"* ")"""
        
#P26
#O/P
"""
*             *
* *         * *
*   *     *   *
* * * * * * * *

n = int(input())

for i in range(0,n):
    if i == 0:
        right_space = "  "*(n-1)
        right_part = "* " + right_space

        left_space = "  "*(n-1)
        left_part = left_space+ "* "
        print(right_part+ left_part)
    elif i == n-1:
        print("* "*(n*2))

    else:
        #left_part
        left_spaces = "  "*(n-i)
        hollow = "  "*(i-1)
        left_part = ("* "+hollow+"* "+left_spaces)
        
        #right_part
        right_space = "  "*(n-i-2)
        hollow = "  "*(i-1)
        right_part = (right_space+"* "+hollow+"* ")
        print(left_part+right_part)"""

#P27
#O/P


"""
*                 *
* *             * *
*   *         *   *
*     *     *     *
*       * *       *
*       * *       *
*     *     *     *
*   *         *   *
* *             * *
*                 *


n = int(input())
#top

for i in range(0,n):
    if i == 0:
        left_top = ("* "+"  "*(n-1))
        right_top = ("  "*(n-1)+"* ")
        print(left_top+right_top)

    else:
        #topleft
        hollow = "  "*(i-1)
        space = "  "*(n-i-1)
        top_left=("* "+hollow+"* "+space)

        #topright
        hollow = "  "*(i-1)
        space = "  "*(n-i-1)
        top_right=(space+"* "+hollow+"* ")

        print(top_left+top_right)

#bottom



for i in range(0,n):
    if i == n-1:
        bottom_left=("* "+"  "*(n-1))
        bottom_right=("  "*(n-1)+"* ")
        print(bottom_left+bottom_right)
    
    else:
        #bottom_left
        hollow = "  "*(n-i-2)
        space ="  "*(i)
        b_l =("* "+hollow+"* "+space) 
        #bottom_right
        hollow = "  "*(n-2-i)
        space = "  "*(i)
        b_r=(space+"* "+hollow+"* ")
        print(b_l+b_r)
"""

#P28
#O/P
"""
    *
   * *
  * * *
 * * * *
* * * * *
 *     *
  *   *
   * *
    *


n = int(input())

for i in range(0,n):
    spaces = " "*(n-i-1)
    star= "* "*(i+1)
    print(spaces+star)


for i in range(1,n):
    if i == n-1:
        print(" "*(n-1)+"* "+" "*(n-2))
    else:
        spaces = " "*(i)
        hollow = " "*((n-2-i)*2)
        print(spaces+"* "+hollow+"* ")"""

#P29
#O/P

"""
        *
      * *
    * * *
  * * * *
* * * * *


n = int(input())

for i in range(0,n):
    space = "  "*(n-i-1)
    stars= ("* "*(i+1))
    print(space+stars)"""

"""
#P30
#O/P

    *
   * *
  * * *
 * * * *
* * * * *

n = int(input())
k = n -1
for i in range(1,n+1):
    spaces = " " *k
    star = "* "*i
    print(spaces+star)
    k = k - 1"""


"""
#O/P
    A
   B B
  C   C
 D     D
E       E
 D     D
  C   C
   B B
    A



n = int(input())

Alpha = 65

for i in range(1,n+1):
    if i == 1:
        print(" "*(n-i)+chr(Alpha))
        Alpha+=1
    else:
        spaces = " " * (n-i)
        hollow = " " * (((i-1)*2)-1)
        print(spaces+chr(Alpha)+hollow + chr(Alpha))
        Alpha+=1

Al = 65 + (n-2)
for j in range(n-1,0,-1):
    if j == 1:
        print(" "*(n-j)+chr(Al))
        Al -=1
    else:
        spaces = " " * (n-j)
        hollow = " " * (((j-1)*2)-1)
        print(spaces+chr(Al)+hollow+chr(Al))
        Al-=1

"""