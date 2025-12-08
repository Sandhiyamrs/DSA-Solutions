from collections import defaultdict, deque

def topological_sort(n, edges):
    graph = defaultdict(list)
    indegree = [0]*n

    for u,v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(n) if indegree[i]==0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    return result

# Example usage
edges = [[0,1],[0,2],[1,3],[2,3],[3,4]]
print("Output:", topological_sort(5, edges))
