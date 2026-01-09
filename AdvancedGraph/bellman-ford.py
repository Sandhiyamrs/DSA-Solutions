def bellman_ford(V, edges, src):
    dist = [float('inf')] * V
    dist[src] = 0

    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # Negative cycle

    return dist
