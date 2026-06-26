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

Patter 2
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
"""
