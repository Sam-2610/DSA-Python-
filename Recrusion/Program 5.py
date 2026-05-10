# Write a Program to print the sum of first n numbers.

def program5(i,total):
    if i < 1:
        print(total)
        return 0
    else:
        program5(i - 1, total + i)

program5(3,0)
