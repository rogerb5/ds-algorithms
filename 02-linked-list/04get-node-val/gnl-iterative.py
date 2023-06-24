class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

def get_node_value(head, index):
  current = head
  count = 0
  while current is not None:
    if count == index:
      return current.val
    count += 1
    current = current.next
  return None

get_node_value(a, 2) # 'c'
