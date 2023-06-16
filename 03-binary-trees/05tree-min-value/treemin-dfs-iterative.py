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

# dfs iterative with stack

def tree_min_value(root):
    smallest = float("inf")
    
    stack = [root]
    while stack:
        current = stack.pop()

        if current.val < smallest: # as soon leaves stack
          smallest = current.val

        if current.left is not None:
         stack.append(current.left)

        if current.right is not None:
         stack.append(current.right)

    print(smallest)
    return smallest

tree_min_value(a) # -> -2
