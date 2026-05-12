# Character Hashing

# Input string
s = input("Enter the string: ")

# Precompute (ASCII size 256)
hash_arr = [0] * 256

for ch in s:
    hash_arr[ord(ch)] += 1   # ord(ch) gives ASCII value

# Number of queries
q = int(input("Enter number of queries: "))

# Process queries
for _ in range(q):
    c = input("Enter character: ")
    print(hash_arr[ord(c)])