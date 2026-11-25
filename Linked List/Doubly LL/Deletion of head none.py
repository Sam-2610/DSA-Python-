class Node:
    def __init__(self, data, next=None, back=None):
        self.data = data
        self.next = next
        self.back = back

def delete_head_node(head):
    if head is None:
        return None

    prev = head
    head = head.next

    if head is not None:
        head.back = None

    prev.next = None

    return head