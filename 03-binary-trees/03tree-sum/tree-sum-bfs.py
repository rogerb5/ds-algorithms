class Node:
    def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None
      
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1


# my solution bfs with a deque
from collections import deque

def tree_sum(root):
    if not root:
        return []
    queue = deque([root])
    values = []
    total_sum = 0
        
    while queue:
        node = queue.popleft()
        total_sum += node.val

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print(total_sum)
    return total_sum

tree_sum(a)
