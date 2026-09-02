"""
def divisor(x):
    for i in range(1,x+1):
        if x % i == 0:
            print(i)
x = int(input("Enter a number: "))
divisor(x) 
"""

def divisor(x):
    ans = []

    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            ans.append(i)

            if i != x // i:
                ans.append(x // i)

    return sorted(ans)


x = int(input("Enter a number: "))
print(divisor(x))