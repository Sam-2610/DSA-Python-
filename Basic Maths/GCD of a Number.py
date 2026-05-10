def gcd_of_a_number():
    a = int(input("Enter the Number : "))
    b = int(input("Enter the Number : "))
    if a == 0: 
        return b
    if b == 0: 
        return a
    while(a > 0 and b > 0):
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    else:
        return a
    
gcd = gcd_of_a_number()
print("The GCD of both numbers is : ",gcd)