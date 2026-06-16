# Problem: Swap two numbers
# Example:
# Input : a = 10, b = 20
# Output: a = 20, b = 10

""" Using third var
a=4
b=5
print(a,b)
c=a
a=b
b=c
print(a,b) """

# Xor wise

a=10
b=20
print(a,b)
a= a^b
b= a^b
a= a^b
print(a,b)