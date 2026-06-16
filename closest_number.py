# Problem: Find the closest multiple of a given number
# Example:
# Input : n = 13, m = 4
# Output: 12

n=int(input("Enter the number:"))
m=int(input("Enter the divisble number:"))

q= n//m
n1 = m*q

if n*m > 0:
    n2= m * (q+1)
else:
    n2 = m * (q-1)

if (abs (n-n1)) < (abs (n-n2)):
    print("Closest number", n1)
else:
    print("Closest number", n2)