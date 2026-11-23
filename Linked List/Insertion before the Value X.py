class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def insert_before_value(head, el, val):
    if head is None:
        return Node(el)

    # Insert before the head
    if head.data == val:
        return Node(el, head)

    current = head

    while current.next is not None:

        # Insert before the target value
        if current.next.data == val:
            new_node = Node(el, current.next)
            current.next = new_node
            break

        current = current.next

    return head