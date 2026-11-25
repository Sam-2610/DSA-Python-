class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def insert_k_element(head, el, k):
    if head is None:
        if k == 1:
            return Node(el)
        else:
            return head

    if k == 1:
        return Node(el, head)

    cnt = 0

    current = head

    while current is not None:
        cnt += 1

        if cnt == k - 1:
            new_node = Node(el, current.next)
            current.next = new_node
            break

        current = current.next

    return head

