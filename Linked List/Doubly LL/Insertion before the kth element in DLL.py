class Node:
    def __init__(self, data, next = None, back = None):
        self.data = data
        self.next = next
        self.back = back

def insert_before_head(head, val):
    new_head = Node(val, head, None)

    if head is not None:
        head.back = new_head

    return new_head

def insert_before_k_element(head, k, val):
    if k == 1:
        return insert_before_head(head, val)

    temp = head
    cnt = 0

    while temp is not None:
        cnt += 1
        if cnt == k:
            break
        temp = temp.next

    if temp is None:
        return head

    prev = temp.back
    new_node = Node(val, temp, prev)
    prev.next = new_node
    temp.back = new_node

    return head