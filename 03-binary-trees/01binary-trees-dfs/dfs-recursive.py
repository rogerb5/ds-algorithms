class Node:
    def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       a
#      / \
#     b   c
#    / \   \
#   d   e   f

# my solution
def depth_first_values(root):
  if not root:
    return []
  
  left_values = depth_first_values(root.left) # [b, d, e]
  right_values = depth_first_values(root.right) # [c, f]
  print([root.val] + left_values + right_values)
  return [root.val] + left_values + right_values

depth_first_values(a)#['a', 'b', 'd', 'e', 'c', 'f']
