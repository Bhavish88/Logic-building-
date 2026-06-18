# Problem: Calculate the factorial of the number
# Example:
# Input : 5
# Output: (5*4*3*2*1) 120

num= int(input("Enter a Number : "))
result = 1
temp = 2

if num == 1 or num==0 :
    result=1

while temp <= num:
    result *= temp
    temp += 1

print("The Factorial is ", result)