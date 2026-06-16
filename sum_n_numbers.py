# Problem: Find the sum of first n natural numbers
# Example:
# Input : 5
# Output: 15

Num= int(input("Enter a natural number: "))
Sum=0
for x in range(1,Num+1):
    Sum= x+Sum

print(Sum)