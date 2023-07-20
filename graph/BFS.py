from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)

        while queue:
            current_node = queue.popleft()
            print(current_node, end=" ")

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)

    start_node = 1
    print("BFS Traversal:")
    graph.bfs(start_node)

