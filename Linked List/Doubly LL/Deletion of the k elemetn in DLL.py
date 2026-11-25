class Node:
    def __init__(self, data, next = None, back = None):
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



def remove_k_element(head, k):
    if head is None:
        return None

    cnt = 0
    kNode = head

    while kNode is not None:
        cnt += 1

        if cnt == k:
            break

        kNode = kNode.next

    if kNode is None:
        return head

    prev = kNode.back
    front = kNode.next

    if prev == None and front == None:
        return None
    elif prev == None:
        return delete_head_node(head)
    elif front == None:
        return delete_tail(head)

    prev.next = front
    front.back = prev

    kNode.next = None
    kNode.back = None

    return head