graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

graph1 = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

# src will represent current position
# graph is a dictonary graph
def has_path(graph, src, dst): 
 if src == dst:
   return True

 for neighbor in graph[src]: # visit neighbors per row
  if has_path(graph, neighbor, dst) == True:
    return True

 return False

print(has_path(graph, 'f', 'k')) # True
print(has_path(graph, 'f', 'j')) # False
print(has_path(graph, 'i', 'h')) # True
print(has_path(graph1, 'v', 'w')) # True
print(has_path(graph1, 'v', 'z')) # False
