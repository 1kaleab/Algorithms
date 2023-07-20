from collections import deque

def bfs(maze, start):
    rows = len(maze)
    cols = len(maze[0])
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if maze[x][y] == 'E':
            return path + [(x, y)]

        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
                    queue.append(((nx, ny), path + [(x, y)]))

    return None

def find_shortest_path(maze):
    rows = len(maze)
    cols = len(maze[0])

    for x in range(rows):
        for y in range(cols):
            if maze[x][y] == 'S':
                start = (x, y)
                break

    path = bfs(maze, start)
    return path

if __name__ == "__main__":
    maze = [
        ['S', '.', '#', '.', '.', '.'],
        ['#', '.', '.', '#', '.', '.'],
        ['.', '.', '#', '.', '#', '.'],
        ['.', '#', '.', '.', '.', '#'],
        ['.', '.', '.', '#', '.', 'E'],
    ]

    # Find the shortest path in the maze
    shortest_path = find_shortest_path(maze)

    if shortest_path:
        # Mark the shortest path in the maze
        for x, y in shortest_path:
            maze[x][y] = '*'

        # Print the maze with the path marked
        for row in maze:
            print(' '.join(row))
    else:
        print("No path found!")

