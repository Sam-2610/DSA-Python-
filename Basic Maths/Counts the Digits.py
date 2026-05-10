def count_the_digits():
    n = int(input("Enter the Number : "))
    count = 0
    while(n > 0):
        count = count + 1
        n = n // 10
    print(f"The Count of Digits in the Number is {count}")

count_the_digits()