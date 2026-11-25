class Node:
    def __init__(self, data, next = None, back = None):
        self.data = data
        self.next = next
        self.back = back

def insert_before_node(node, val):
    prev = node.back
    new_node = Node(val, node, prev)

    if prev is not None:
        prev.next = new_node

    node.back = new_node

    return new_node