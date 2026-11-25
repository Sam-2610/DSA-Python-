class Node:
    def __init__(self, data, next=None, back=None):
        self.data = data
        self.next = next
        self.back = back

def convert_in_arr(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        current = Node(arr[i], None, prev)
        prev.next = current
        prev = current

    return head


arr = [10, 20, 30, 40, 50]

head = convert_in_arr(arr)