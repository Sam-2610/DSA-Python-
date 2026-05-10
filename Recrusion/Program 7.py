# Write a Program to Print the Fibnaachi Number.

def program7(n):
    if n <= 1:
        return n
    else:
        last = program7(n - 1)
        start = program7(n - 2)
        return last + start
    
f = program7(4)
print(f)