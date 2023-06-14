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

# depth first search solution using a stack(under the hood) and recursion
def has_path(graph, src, dst): 
  if src == dst:
    return True
  
  for neighbor in graph[src]: # iterate through the neighbors
   if has_path(graph, neighbor, dst) == True:
    return True

  return False

print(has_path(graph, 'f', 'k')) # True
print(has_path(graph, 'f', 'j')) # False
print(has_path(graph, 'i', 'h')) # True
print(has_path(graph1, 'v', 'w')) # True
print(has_path(graph1, 'v', 'z')) # False


