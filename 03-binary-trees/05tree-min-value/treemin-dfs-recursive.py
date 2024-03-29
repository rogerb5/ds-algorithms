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

def tree_min_value(root):
    if root is None:
     return float("inf")

    min_left = tree_min_value(root.left)
    min_right = tree_min_value(root.right)

    return min(root.val, min_left, min_right)

tree_min_value(a) # -> -2
