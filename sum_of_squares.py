# Problem: Find the sum of squares of first n natural numbers
# Example:
# Input : 3
# Output: 14
# Explanation: 1² + 2² + 3² = 14

Num= int(input("Enter a natural number: "))
Sum = 0
for x in range(1,Num+1):
    Sum= x**2 +Sum

print(Sum)

# for time optimisation O(n):

Num= int(input("Enter a natural number: "))
sum_of_square = Num*(Num+1)*(2*Num+1)//6
print(sum_of_square)
