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
  
  stack = [root] # stack stores instances of node elements
  values = []
  
  while stack:
    node = stack.pop()
    values.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)

  print(values)
  return values
            
depth_first_values(a)
