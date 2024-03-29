class Node:
    def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None
      
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

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

# my solution using a list
# in python pop() from a list is o(n) time since shifting occurs
# and appending is in o(1) time
# therefore, the total operation is costly and not optimal at o(n^2)
def breadth_first_values(root):
    if root is None:
        return []

    values = []
    queue = [ root ] # begin list with root node
    while queue:
        current = queue.pop(0)
        values.append(current.val)
        
        if current.left:
            queue.append(current.left)
            
        if current.right:
            queue.append(current.right)

    print(values)
    return values

breadth_first_values(a) #['a', 'b', 'c', 'd', 'e', 'f']
