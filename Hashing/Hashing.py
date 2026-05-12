# WAP to Count the Frequencies of Number in an Array.

def hashing():
    n = int(input("Enter the Value of n : "))
    arr = []
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)

    hash_dict : dict[int,int] = {}
    
    for num in arr:
        if num in hash_dict:
            hash_dict[num] += 1
        else:
            hash_dict[num] = 1

    q = int(input("Enter the Queries : "))
    for _ in range(q):
        number = int(input("Enter the Number : "))
        print(hash_dict.get(number,0))

hashing()