class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_k_element(head, k):
    if head is None:
        return None

    # Remove the head node
    if k == 1:
        return head.next

    cnt = 0
    current = head
    prev = None

    while current is not None:
        cnt += 1

        # Remove the kth node by updating the previous node's pointer
        if cnt == k:
            if prev is not None:
                prev.next = current.next
            break

        prev = current
        current = current.next

    return head

"""T.C = 0(1), S.C = 0(1)"""