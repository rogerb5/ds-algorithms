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

def linked_list_find(head, target):
  
 if head is None: # order of ifs matter
   return False
 if head.val == target:
   return True
 return linked_list_find(head.next, target)
  

linked_list_find(a, "c") # true
