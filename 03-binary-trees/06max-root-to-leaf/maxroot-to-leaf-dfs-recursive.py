class Node:
    def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None
      
a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       5
#    /    \
#   11     3
#  / \      \
# 4   2     1

def max_path_sum(root):
  if root is None:
      return float("-inf")

  if root.left is None and root.right is None:
      return root.val

  max_left = max_path_sum(root.left)
  max_right = max_path_sum(root.right)

  print(root.val + max(max_left, max_right))
  return root.val + max(max_left, max_right)

max_path_sum(a) # 20
