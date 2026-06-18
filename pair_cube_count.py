# Problem: Given n, count all 'a' and 'b' that satisfy the condition a^3 + b^3 = n. Where (a, b) and (b, a) are considered two different pairs
# Example:
# Input : 9
# Output: 2 (1^3 + 2^3 = 9 and 2^3 + 1^3 = 9)

def num_count():
    num=int(input("Enter a Number : "))
    count = 0

    for a in range(1, num+1 ):
        for b in range(num+1):
            if a**3 + b**3 == num :
                count += 1
    print("Total count", count)

num_count()