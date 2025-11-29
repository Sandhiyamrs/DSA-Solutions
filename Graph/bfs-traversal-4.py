from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])
    visited.add(start)
    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

    return result

# Test
graph = {0:[1,2], 1:[0,3], 2:[0,4], 3:[1], 4:[2]}
print(bfs(graph, 0))  # Output: [0,1,2,3,4]
