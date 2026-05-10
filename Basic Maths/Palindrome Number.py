def palindrome_number():
    n = int(input("Enter the Number : "))
    rev = 0
    dup = n
    while(n > 0):
        last_digit = n % 10
        rev = rev * 10 + last_digit
        n = n // 10
    if(dup == rev):
        print("Palindrome Number")
    else:
        print("Not a Palindrome")

palindrome_number()