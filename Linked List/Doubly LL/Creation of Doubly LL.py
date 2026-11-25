class Node:
    def __init__(self, data, next = None, back = None):
        self.data = data
        self.next = next
        self.back = back

def main():
        arr = [2,5,8,7]
        y = Node(arr[0])
        print(y)
        print(y.data)

if __name__ == "__main__":
        main()