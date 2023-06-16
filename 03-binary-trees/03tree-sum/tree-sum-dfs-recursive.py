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

# should result in 21
# 3 + 13 + 5 => 21

# my solution recursive dfs
def tree_sum(root):
  if root is None:
    return 0
  return root.val + tree_sum(root.left) + tree_sum(root.right)

tree_sum(a) # 21
