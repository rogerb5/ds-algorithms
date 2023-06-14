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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f


# bfs queue solution

from collections import deque

def tree_includes(root, target):
    if root is None:
        return False

    queue = deque([root])

    while queue:
     current = queue.popleft()
     if current.val == target:
        return True
        
     if current.left:
        queue.append(current.left)

     if current.right:
         queue.append(current.right)
         
    return False

tree_includes(a, "e")
