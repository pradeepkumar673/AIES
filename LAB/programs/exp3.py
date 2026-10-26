# Implement Uniform Cost Search (UCS) Algorithm.

import heapq

def ucs(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return cost, path
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path + [neighbor]))
    return float('inf'), []

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 4)],
    'G': []
}

cost, path = ucs(graph, 'A', 'G')
print("UCS - Minimum Cost:", cost)
print("UCS - Path:", path)
