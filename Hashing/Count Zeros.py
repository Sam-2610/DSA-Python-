# WAP to Count the Number of Zeros in an Array.

def count_zeros():
    arr = []
    count = 0
    n = int(input("Enter the Number : "))
    for i in range(n):
        x = int(input(f"Enter the Element {i + 1} : "))
        arr.append(x)
    
    for num in arr:
        if num == 0:
            count = count + 1
    if count:
        print(f"The Count of Zeros is : {count}")
    else:
        print("No Zeros")
            
        

count_zeros()
        
    