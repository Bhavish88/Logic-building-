# Problem: Find the sum of digits of a number
# Example:
# Input : 1234
# Output: 10

num = int(input("Enter a number :"))
sum = 0

while num != 0:
    num_2 = int (num % 10)
    sum = sum + num_2
    num = num / 10

print("Total sum", sum)