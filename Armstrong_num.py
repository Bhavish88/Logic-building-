class solution:
    def armstrong(x):
        ans = x
        num = 0
        temp = x
        digit=0
        while temp > 0:
            temp//=10
            digit+=1
        while x != 0:
            last_dig = x % 10
            arm = last_dig**digit
            num = num+arm
            x //= 10 
        if ans == num:
            return True
        else:
            return False
    x = int(input("Enter a number: "))
    print(armstrong(x))