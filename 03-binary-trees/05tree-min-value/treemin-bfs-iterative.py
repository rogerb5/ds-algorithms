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

# bfs using a deque
from collections import deque

def tree_min_value(root):
    smallest = float("inf")
    queue = deque([root])

    while queue:
        current = queue.popleft()
        if current.val < smallest:
         smallest = current.val

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    print(smallest)
    return smallest

tree_min_value(a) # -> -2
