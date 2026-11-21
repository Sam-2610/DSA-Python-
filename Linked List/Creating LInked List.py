class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def main():
        arr = [2,5,8,7]
        y = Node(arr[0])
        print(y)
        print(y.data)

if __name__ == "__main__":
        main()
        