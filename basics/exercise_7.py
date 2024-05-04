# Check Palindrome Number
def check_palindrome(num): 
    c=str(num)
    rev=c[::-1]
    if (int(num)==int(rev)):
        print(str(num) + " is a palindrome")
    else:
        print(str(num) + " is not a palindrome")
    
a=211
b=121
check_palindrome(a)
check_palindrome(b)
