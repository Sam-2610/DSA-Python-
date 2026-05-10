# Write a Program to Print 5 to 1

def program4(i,n):
    if i < 1:
        return
    print(i,end=" ")
    program4(i - 1,n)

program4(5,5)
    