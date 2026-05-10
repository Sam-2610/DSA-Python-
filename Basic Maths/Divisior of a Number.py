def divisor_of_a_number():
    n = int(input("Enter the Number : "))
    for i in range(1,n + 1):
        if n % i == 0:
            print(i,end=" ")

divisor_of_a_number()