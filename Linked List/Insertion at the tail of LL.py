class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def insert_tail(head, newdata):
    if head is None:
        return Node(newdata)

    current = head

    while current.next is not None:
        current = current.next

    new_Node = Node(newdata)
    current.next = new_Node
    return head

# Create a linked list from user input
def create_ll(arr):
    head = None

    for i in arr:
        head = insert_tail(head, i)

    return head


# Print the linked list
def print_ll(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Take input
arr = list(map(int, input("Enter elements: ").split()))

head = create_ll(arr)
print_ll(head)