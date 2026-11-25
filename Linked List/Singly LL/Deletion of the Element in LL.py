class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_element(head, el):
    if head is None:
        return None

    # Remove the head if it contains the target element
    if head.data == el:
        return head.next

    current = head
    prev = None

    while current is not None:

        # Remove the node by connecting the previous node to the next node
        if current.data == el:
            if prev is not None:
                prev.next = current.next
            break

        # Move both pointers forward
        prev = current
        current = current.next

    # Return the updated head of the linked list
    return head

"""T.C = 0(1), S.C = 0(1)"""