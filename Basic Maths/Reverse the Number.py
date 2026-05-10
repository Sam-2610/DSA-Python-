def reverse_the_number():
    n = int(input("Enter the Digit : "))
    rev = 0
    while(n > 0):
        last_digit = n % 10
        rev = rev * 10 + last_digit
        n = n // 10
    print(f"The Reverse of the Number is {rev}")

reverse_the_number()