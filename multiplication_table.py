# Problem: Print the multiplication table of a number
# Example:
# Input : 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...

num = int(input("Enter a Number:"))

for x in range(1,11):
    print(num*x)
    x = x+1
    