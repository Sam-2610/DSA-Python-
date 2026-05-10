# Write a Program to Check the Palindrome 

def program8(i, s):
    if i >= len(s) / 2:
        return True
    if s[i] != s[len(s) - i - 1]:
        return False
    return program8(i + 1, s)

s = input("Enter the String : ").lower()
n = program8(0, s)
print(n)
        