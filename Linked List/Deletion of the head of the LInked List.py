class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def delete_head(head):
    if head is None:
        return None
    return head.next


"""Space Complexity (SC): (O(1), Time Complexity (TC): (O(1)"""