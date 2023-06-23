# recursive approach

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

# The two function split
# so we can recursivley add to a single values list
def linked_list_values(head):
 values = []
 fill_values(head, values)
 print(values)
 return values

def fill_values(head, values):
 if head is None:
  return

 values.append(head.val)
 fill_values(head.next, values)

linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]
