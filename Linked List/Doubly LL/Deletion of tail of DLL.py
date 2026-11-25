class Node:
    def __init__(self, data, next = None, back = None):
        self.data = data
        self.next = next
        self.back = back

def delete_tail(head):
    if head is None or head.next is None:
        return None

    tail = head

    while tail.next is not None:
        tail = tail.next

    new_tail = tail.back
    new_tail.next = None
    tail.back = None

    return head