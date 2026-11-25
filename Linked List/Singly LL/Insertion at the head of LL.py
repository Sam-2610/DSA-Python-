class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert_head(head, newdata):
    new_Node = Node(newdata, head)
    return new_Node


# Create a linked list from user input
def create_ll(arr):
    head = None

    for i in arr:
        head = insert_head(head, i)

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