# Write a function, has_path, that takes in a dictionary representing
# the adjacency list of a directed acyclic graph and two nodes (src, dst).
# The function should return a boolean indicating whether
# or not there exists a directed path between the source and destination nodes.

# DAG visual representation
# (f)--->(g)--->(h)
#  |     ^
#  |    /
#  |   /
#  v  /
# (i)<-----(j)
#  | 
#  |
#  |
#  v
# (k)

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}


# DAG visual representation
# (v)--->(x)
#  |
#  |
#  v
# (w)

# (y)--->(z)

graph1 = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

# a deque (double ended queue) in python
# is implemented using module "collections"
# Restrictions: Input Restricted Deque:
# Input is limited at one end while deletion is permitted at both ends.

# Output Restricted Deque: output is limited at one end
# but insertion is permitted at both ends

# example
# back [10][15][20][30][40][50][60][70] front
# popleft()                             pop()
# appendleft()                          append()

from collections import deque

def has_path(graph, src, dst):
  queue = deque([ src ])
  
  while queue:
    current = queue.popleft()
    if current == dst:
      return True
    
    for neighbor in graph[current]:
      queue.append(neighbor)
    
  return False


print(has_path(graph, 'f', 'k')) # True
print(has_path(graph, 'f', 'j')) # False
print(has_path(graph, 'i', 'h')) # True
print(has_path(graph1, 'v', 'w')) # True
print(has_path(graph1, 'v', 'z')) # False


