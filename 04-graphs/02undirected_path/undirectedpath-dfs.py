def undirected_path(edges, node_A, node_B):
 graph = build_graph(edges)
 # print(graph) adjacency list
 return has_path(graph, node_A, node_B, set()) # a set gives u O(1) look and insertion
 
def has_path(graph, src, dst, visited):
 if src == dst:
  return True

 if src in visited:
  return False

 visited.add(src) # add src after you check! After checking

 for neighbor in graph[src]: # key into graph you get neigbors list of src
  if has_path(graph, neighbor, dst, visited) == True:
    return True

 return False
 
# convert edge graph to adjacency list
def build_graph(edges):
 graph = {} # dictonary

 for edge in edges:
  a, b = edge
  if a not in graph:
   graph[a] = []
  if b not in graph:
    graph[b] = []

  graph[a].append(b)
  graph[b].append(a)

 return graph

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'j', 'm') # -> True
