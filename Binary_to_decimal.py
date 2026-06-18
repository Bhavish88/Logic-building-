# Problem: Given a non negative number n, the task is to convert the given number into an equivalent binary representation.
# Example:
# Input : 12
# Output: 1100

def decToBin(n):
    binarr = []

    while n > 0:
        bit = n%2 
        binarr.append(str(bit))
        n //= 2
    binarr.reverse()
    return "".join(binarr)

print(decToBin(13))

