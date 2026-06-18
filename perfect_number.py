# Problem: A number is a perfect number if it is equal to the sum of its proper divisors, that is, the sum of its positive divisors excluding the number itself. Find whether a given positive integer n is perfect or not.
# Example:
# Input : 15
# Output: False

def isperfect():
    num=int(input("Enter a number : "))
    sum = 0

    for x in range (1, num):
        if num % x == 0:
            sum += x
      
    if sum == num:
        print("The number is a Perfect Number.")
    else:
        print("The number is not a Perfect Number.")

isperfect()