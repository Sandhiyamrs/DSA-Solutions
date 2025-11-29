from collections import defaultdict

def kosaraju_scc(graph):
    n = len(graph)
    visited = set()
    order = []

    def dfs1(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs1(v)
        order.append(u)

    for u in graph:
        if u not in visited:
            dfs1(u)

    # Transpose graph
    transpose = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transpose[v].append(u)

    visited.clear()
    scc = []

    def dfs2(u, component):
        visited.add(u)
        component.append(u)
        for v in transpose[u]:
            if v not in visited:
                dfs2(v, component)

    for u in reversed(order):
        if u not in visited:
            comp = []
            dfs2(u, comp)
            scc.append(comp)

    return scc

# Test
graph = {0:[1],1:[2],2:[0],3:[2,4],4:[3]}
print(kosaraju_scc(graph))  # Output: [[0,1,2],[3,4]]
