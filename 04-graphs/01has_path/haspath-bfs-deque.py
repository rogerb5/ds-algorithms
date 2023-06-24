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

# bfs solution iteratively
from collections import deque

def has_path(graph, src, dst):
  queue = deque([src])
  
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
