class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def delete_head(head):
    if head is None:
        return None
    return head.next

    