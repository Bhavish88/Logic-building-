# Problem: Reverse the digits of a number
# Example:
# Input : 123
# Output: 321

num = int(input("Enter a number :"))
sum = 0

while num != 0:
    num_2 = num % 10
    sum= sum * 10 + num_2
    num = num // 10

print(sum)
