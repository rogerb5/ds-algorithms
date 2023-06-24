# iterative code will help us hop
# disconnected components
# dfs code that explores a single component
# as far as possible
def largest_component(graph):
 visited = set()
 largest = 0
    
 for node in graph:
  size = explore_size(graph, node, visited) # explore as far as possible, return number
  if size > largest:
   largest = size
 return largest

def explore_size(graph, node, visited):
 # gaurd against infinite loops
 if node in visited:
  return 0 # if node has been visited do not double count it

 visited.add(node) # set gives you O(1) lookup and insertion

 size = 1 # one reprsents the node im at right now 
 for neighbor in graph[node]:
  size += explore_size(graph, neighbor, visited) # how big entire connected graph is

 return size

print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 4

# where you need to hop 
# you will need a helper function that will explore a component
# and code that helps you begin a traversal on seperate components (islands)
