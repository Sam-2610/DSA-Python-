# Not Equal elements Rnadom Positive and Negative Elements 

def rearrangeArray():
    arr1 =[]
    n = int(input("Enter the Number of Element : "))
    for i in range(n):
        x = int(input(f"Enter the Elements {i + 1} : "))
        arr1.append(x)

    positive = []
    negative = []

    for i in range(n):
        if arr1[i] > 0:
            positive.append(arr1[i])
        else:
            negative.append(arr1[i])
    
    if len(positive) > len(negative):
        for i in range(len(negative)):
            arr1[2*i] = positive[i]
            arr1[2*i+1] = negative[i]

        index = len(negative)*2
        for i in range(len(negative),len(positive)):
            arr1[index] = positive[i]
            index = index + 1
    else:
        for i in range(len(positive)):
            arr1[2*i] = positive[i]
            arr1[2*i+1] = negative[i]
        index = len(positive) * 2
        for i in range(len(positive),len(negative)):
            arr1[index] = negative[i]
            index = index + 1
    print(arr1)


rearrangeArray()