def gcd(x,y):
    
    gcd=1 
    for i in range(1, min(x,y)):
        if x % i == 0 and y % i == 0:
            gcd = i
    print("gcd is :", gcd)

x = int(input("Enter Number 1:"))
y = int(input("Enter Number 2:"))
gcd(x,y)