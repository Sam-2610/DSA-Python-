class Node:
    def __init__(self, data, next = None, back = None):
        self.data = data
        self.next = next
        self.back = back

def reverse_ddl(head):
    if head is None or head.next is None:
        return head

    current = head

    while current is not None:
        current.back, current.next = current.next, current.back
        current = current.back

    return head.back