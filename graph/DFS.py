# Graph represented as an adjacency list
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2],
    6: [3],
    7: [3]
}
def dfs_recursive(vertex, visited):
    visited[vertex] = True
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs_recursive(neighbor, visited)


def depth_first_search_recursive(start_vertex):
    visited = {vertex: False for vertex in graph}
    dfs_recursive(start_vertex, visited)
    print()  # New line after DFS traversal


# Example usage:
print("DFS Traversal (Recursive):")
depth_first_search_recursive(1)

def depth_first_search_iterative(start_vertex):
    visited = {vertex: False for vertex in graph}
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            print(vertex, end=" ")

            # Push unvisited neighbors to the stack
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    stack.append(neighbor)

    print()  # New line after DFS traversal


# Example usage:
print("DFS Traversal (Iterative):")
depth_first_search_iterative(1)

