class Node:
    def __init__(self, data, next=None, back=None):
        self.data = data
        self.next = next
        self.back = back

def insert_before_tail(head, val):
    if head is None:
        return Node(val)

    if head.next is None:
        return Node(val, head, None)

    tail = head

    while tail.next is not None:
        tail = tail.next

    prev = tail.back
    new_node = Node(val, tail, prev)

    prev.next = new_node
    tail.back = new_node

    return head