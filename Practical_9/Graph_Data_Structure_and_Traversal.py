# 1.Implementing the Graph Class
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1) 
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()

# 2.Implementing Depth-First Search (DFS)
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1) 
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("\nDFS starting from vertex 0:")
g.dfs(0)

# 3.Implementing Breadth-First Search (BFS)
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1) 
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("\nBFS starting from vertex 0:")
g.bfs(0)

# 4.Implementing a Method to Find All Paths
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1) 
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))

# 5.Implementing a Method to Check if the Graph is Connected
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1) 
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("\nIs the graph connected?", g.is_connected())

g.add_vertex(4)
print("After adding a disconnected vertex:")
print("Is the graph connected?", g.is_connected())

# Exercises
# 1.Finding the shortest path between two vertices using BFS.
from collections import deque

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])]) 
    visited = set()
    
    while queue:
        current_vertex, path = queue.popleft() 
        if current_vertex == goal:
            return path 
        visited.add(current_vertex)
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None 

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    start_vertex = 'A'
    goal_vertex = 'F'
    path = bfs_shortest_path(graph, start_vertex, goal_vertex)
    
    if path:
        print("Shortest path from {} to {}: {}".format(start_vertex, goal_vertex, path))
    else:
        print("No path exists from {} to {}".format(start_vertex, goal_vertex))

# 2.Adding a method to detect cycles in the graph.
def has_cycle_undirected(graph):
    def dfs(v, parent):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                if dfs(neighbor, v):
                    return True
            elif parent != neighbor:
                return True
        return False

    visited = set()
    
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False

graph_undirected = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
}

print(has_cycle_undirected(graph_undirected)) 