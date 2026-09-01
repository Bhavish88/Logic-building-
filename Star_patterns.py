"""
Pattern 1
****
****
****
****
****
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

Pattern 2
* 
* * 
* * * 
* * * * 
* * * * * 
for i in range(1,6):
    for j in range(i):
        print("* ", end="")
    print()

Pattern 3 
1
12
123
1234
12345
for i in range(1, 6):
    for j in range(1, i+1):
        print( j ,end="")
    print()


Pattern 4
1
22
333
4444
55555
def pattern_4():
    for i in range(6):
        for j in range(i):
            print(i , end="")
        print()
pattern_4()

pattern 5
*****
****
***
**
*
num = 5
for i in range(1,num+1):
    for j in range(num-i+1):
        print("*", end="")
    print()

pattern 6
12345
1234
123
12
1
num = 5
for i in range(num):
    for j in range(1,num-i+1):
        print(j, end="")
    print()

pattern 7
    *    
   ***   
  *****  
 ******* 
*********
n = 5
for i in range(n):
    # for space
    for j in range(n-i-1):
        print(" ",end="")
    # for star 
    for j in range(2*i+1):
        print("*",end="")
    print()

Pattern 8
*********
 *******
  *****
   ***
    *
n = 5
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(2*n-(2*i+1)):
        print("*",end="")
    print()


pattern 9 
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
n=5 
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(2*n-(2*i+1)):
        print("*",end="")
    print()
    
Pattern 10
*
**
***
****
*****
****
***
**
*

n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print("*",end="")
    print()



Pattern 11
1
01
101
0101
10101

n = 5 
start= 1
for i in range(n):
    if i%2==0:
        start = 1
    else:
        start = 0
    for j in range(i+1):
        print(start,end="")
        start = 1 - start 
    print()

Pattern 12
1      1
12    21
123  321
12344321

n=4
for i in range(1,n+1):
    # number
    for j in range(1, i+1):
        print(j,end="")

    # space
    for j in range(2*(n-i)):
        print(" ",end="")

    # number
    for j in range(i, 0, -1):
        print(j,end="")

    print()

Pattern 13
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
n= 5
start=1
for i in range(1,n+1):
    for j in range(i):
        print(start , end=" ")
        start+=1
    print()


Pattern 14
A 
A B 
A B C 
A B C D 
A B C D E 
n= 5
start= ord("A")
for i in range(1,n+1):
    for j in range(i):
        print(chr(start+j) , end=" ")
    print()


Pattern 15
A B C D E 
A B C D 
A B C 
A B 
A 

n= 5
start= ord("A")
for i in range(n,0,-1):
    for j in range(i):
        print(chr(start+j) , end=" ")
    print()

Pattern 16
A 
B B 
C C C 
D D D D 
E E E E E 

n= 5
start= ord("A")
for i in range(1, n+1):
    for j in range(i):
        print(chr(start) , end=" ")
    print()
    start+=1


Pattern 18
E 
D E 
C D E 
B C D E 
A B C D E 
n = 5

for i in range(1, n + 1):
    start = ord("E") - i + 1

    for j in range(i):
        print(chr(start + j), end=" ")

    print()



Pattern 19
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
n=5
space=0
for i in range(n):
    #for star
    for j in range(n-i):
        print("*", end=" ")
    #for space
    for j in range(space):
        print(" ",end=" ")
    #for star
    for j in range(n-i):
        print("*", end=" ")
    space+=2
    print()
space=8
for i in range(1,n+1):
    #for star
    for j in range(i):
        print("*", end=" ")
    #for space
    for j in range(space):
        print(" ",end=" ")
    #for star
    for j in range(i):
        print("*", end=" ")
    space-=2
    print()



Pattern 20
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
n=5 
space=8
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    for j in range(space):
        print(" ", end=" ")
    for j in range(i):
        print("*",end=" ")
    space-=2
    print()
space=2
for i in range(1,n):
    for j in range(n-i):
        print("*", end=" ")
    for j in range(space):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    space+=2
    print()

Pattern 21
* * * * 
*     * 
*     * 
* * * * 
n=4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
"""

