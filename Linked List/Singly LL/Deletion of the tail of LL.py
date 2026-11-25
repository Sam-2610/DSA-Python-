class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def delete_tail(head):
    if head is None or head.next is None:
        return None

    current = head

    while current.next.next is not None:
        current = current.next

    current.next = None
    return head

"""T.C = 0(n), S.C = 0(1)"""