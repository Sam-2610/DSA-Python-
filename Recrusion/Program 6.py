# Write a Program to Print Factorial of a Number.

def program6(n):
    if n == 0:
        return 1
    else: 
        return n * program6(n - 1)
    
fact = program6(5)
print(fact)