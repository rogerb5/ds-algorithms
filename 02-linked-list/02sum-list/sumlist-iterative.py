class Node:
 def __init__(self, val):
   self.val = val
   self.next = None

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

# Just pay attention to the current node
# do not look ahead and assumption of list length
def sum_list(head):
 total_sum = 0

 current = head
 while current is not None:
  total_sum += current.val
  current = current.next
  
 print(total_sum)
 return total_sum

sum_list(a)
