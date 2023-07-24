# DFS 알고리즘


def dfs(graph, x, visited):
    visited[x] = True
    for y in graph[x]:
        if visited[y] == False:
            dfs(graph, y, visited)
