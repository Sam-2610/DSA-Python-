def armstrong_number():
    n = int(input("Enter the Number : "))
    original = n
    sum = 0
    while(n > 0):
        last_digit = n % 10
        sum = sum + last_digit ** 3
        n = n // 10
    if original == sum : 
        print("Armstrong Number")
    else : 
        print("Not an Armstrong Number")

armstrong_number()