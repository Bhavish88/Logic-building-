"""
Example 1:
Input:N = 12345
Output:5
Explanation:  The number 12345 has 5 digits.
                        
Example 2:
Input:N = 7789              
Output: 4
Explanation: The number 7789 has 4 digits.
"""

Num= int(input("Enter a number: "))
Total_number= 0
while Num>0:
    Last_Digit = Num%10
    Num = Num // 10
    Total_number+=1

print("Output: ", Total_number)