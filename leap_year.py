# Problem: Check whether a year is a leap year
# Example:
# Input : 2024
# Output: Leap Year

Year = int(input("Enter a Year:"))

if Year % 400 == 0 or Year % 4 == 0 and Year % 100 != 0:
    print("Year is a leap year")
else:
    print("Year is not a leap year")