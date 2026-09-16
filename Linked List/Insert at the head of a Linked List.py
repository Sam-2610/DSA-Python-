class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def inserthead(head, newdata):
    newnode = Node(newdata, head)
    return newnode


def printlist(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


def main():
    head = Node(2)
    head.next = Node(3)

    head = inserthead(head, 1)
    printlist(head)


if __name__ == "__main__":
    main()