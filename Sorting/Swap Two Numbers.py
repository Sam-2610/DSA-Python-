# WAP to Swap two Numbers.

def swap_numbers():
    a = int(input("Enter the Value of a : "))
    b = int(input("Enter the Value of b : "))
    temp = a
    a = b
    b = temp
    print(f"The Value of a : {a}")
    print(f"The Value of b : {b}")

swap_numbers()