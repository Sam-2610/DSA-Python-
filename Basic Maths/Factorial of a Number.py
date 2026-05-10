def factorial_of_a_number():
    n = int(input("Enter the Number : "))
    factorial = 1
    while(n != 0):
        factorial = factorial * n
        n = n - 1
    print(f"The Factorial of a Number is {factorial}")

factorial_of_a_number()