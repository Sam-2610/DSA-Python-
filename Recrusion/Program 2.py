# Write a Program to print 5 times

def program2(i,n):
    if i > n:
        return
    print("Hello World")
    program2(i + 1,n)

program2(1,5)