
import collections

# --- Linked List ---
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"

def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

# --- Binary Tree ---
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

def list_to_binary_tree(arr):
    """
    Constructs a binary tree from a list using BFS (LeetCode style).
    [1, 2, 3, null, 4] -> 
       1
      / \
     2   3
      \
       4
    """
    if not arr:
        return None
    
    iter_arr = iter(arr)
    root = TreeNode(next(iter_arr))
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        
        # Left Child
        try:
            val = next(iter_arr)
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
        except StopIteration:
            break
            
        # Right Child
        try:
            val = next(iter_arr)
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
        except StopIteration:
            break
            
    return root

def binary_tree_to_list(root):
    """
    Serializes a binary tree to a list using BFS (LeetCode style).
    Trims trailing None values.
    """
    if not root:
        return []
    
    result = []
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
            
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
        
    return result
