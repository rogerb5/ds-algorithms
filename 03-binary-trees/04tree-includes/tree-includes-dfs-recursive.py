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


# dfs recursive solution

def tree_includes(root, target):
    # start base case
    if root is None:
        return False

    # target is immediately found
    if root.val == target:
        return True
    
    return tree_includes(root.left, target) or tree_includes(root.right, target)

tree_includes(a, "e")
