class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

def zipper_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None

  if head_1 is None:
    return head_2

  if head_2 is None:
    return head_1

  next_1 = head_1.next
  next_2 = head_2.next
  
  head_1.next = head_2
  head_2.next = zipper_lists(next_1, next_2)
  return head_1
  
zipper_lists(a, x) # a -> x -> b -> y -> c -> z
