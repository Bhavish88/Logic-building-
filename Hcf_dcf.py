# Problem: Given two positive integers a and b, the task is to find the GCD of the two numbers.
# Example:
# Input : a = 20, b = 28
# Output: 4 
import math

def hcf():
    n1= int(input("Enter first number : "))
    n2= int(input("Enter second number : "))

    print("The Gcd is :", math.gcd(n1,n2))

hcf()