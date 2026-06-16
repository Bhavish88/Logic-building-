# Problem: Check whether a number is prime
# Example:
# Input : 13
# Output: Prime Number

num = int(input(" Enter a Number:"))
isPrime= True

if num <= 1:
    isPrime = False

else:
    for x in range (2, num):
        if num % x == 0:
            isPrime = False
            break

if isPrime == True:
    print("Prime Number")
else:
    print("Not a Prime number")