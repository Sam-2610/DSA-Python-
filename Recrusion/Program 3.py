# Write a Program to print 1 to 5.

def program3(i,n):
    if i > n:
        return
    print(i,end=" ")
    program3(i + 1,n)

program3(1,5)