class Node:
    def __init__(self, data, next=None, back=None):
        self.data = data
        self.next = next
        self.back = back

def delete_Node(temp):
    prev = temp.back
    front = temp.next

    # Delete tail node
    if front is None:
        prev.next = None
        temp.back = None
        return

    # Connect previous and next nodes
    prev.next = front
    front.back = prev

    # Disconnect the deleted node
    temp.next = None
    temp.back = None