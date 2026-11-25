class Node:
    def __init__(self, data, next = None, back = None):
        self.data = data
        self.next = next
        self.back = back

def insert_before_head(head, val):
    new_head = Node(val, head, None)
    head.back = new_head

    return new_head