import graph
import sys
from collections import deque


# Helper function to perform BFS and find shortest paths
def bfs_shortest_paths(graph, start, end):
    visited = [-1] * graph.n
    visited[start] = 0
    queue = deque([start])
    predecessors = {start: []}

    while queue:
        u = queue.popleft()

        for v in graph.adj[u]:
            if visited[v] == -1:
                visited[v] = visited[u] + 1
                predecessors[v] = [u]
                queue.append(v)
            elif visited[v] == visited[u] + 1:
                predecessors[v].append(u)

    return visited, predecessors


# Function to backtrack from the end vertex to find all shortest paths
def find_paths(predecessors, start, end):
    def build_path(v, path):
        if v == start:
            all_paths.append(path)
            return
        for u in predecessors[v]:
            build_path(u, [u] + path)

    all_paths = []
    if end in predecessors:
        build_path(end, [end])
    return all_paths


# Main algorithm to find the maximum number of vertices in B on any shortest path
def algorithm(graph, B, start, end):
    visited, predecessors = bfs_shortest_paths(graph, start, end)
    if visited[end] == -1:
        return 0

    all_shortest_paths = find_paths(predecessors, start, end)
    print("All Shortest Paths:", all_shortest_paths)

    max_B_count = 0
    for path in all_shortest_paths:
        B_count = sum(vertex in B for vertex in path[:-1]) + (end in B)
        print("Path:", path, "B Count:", B_count)

        max_B_count = max(max_B_count, B_count)

    return max_B_count


# Function to read a set of vertices from a file
def readset(filename):
    with open(filename, "r") as f:
        return {int(v) for line in f for v in line.split()}


# Function to read a pair of vertices from a file
def readpair(filename):
    with open(filename, "r") as f:
        v, w = next(f).split()
        return int(v), int(w)


if __name__ == "__main__":
    g = graph.Graph()
    g.readgraph(sys.argv[1])
    B = readset(sys.argv[2])
    s, t = readpair(sys.argv[3])

    result = algorithm(g, B, s, t)
    print(
        f"Maximum number of vertices from B on a shortest path from {s} to {t}: {result}"
    )
