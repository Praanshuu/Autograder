class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_cycle(n, values, pos):
    # Create linked list
    nodes = [ListNode(val) for val in values]

    for i in range(n - 1):
        nodes[i].next = nodes[i + 1]

    # Create cycle if pos != -1
    if pos != -1:
        nodes[-1].next = nodes[pos]

    head = nodes[0] if n > 0 else None

    # Floyd’s Cycle Detection Algorithm
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

