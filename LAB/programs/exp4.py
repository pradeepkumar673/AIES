# Implement Best First Search Algorithm.

import heapq

def best_first_search(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], start, [start])]
    visited = set()

    while priority_queue:
        h, node, path = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))
    return []

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

heuristic = {
    'A': 6, 'B': 4, 'C': 5,
    'D': 2, 'E': 3, 'F': 4,
    'G': 0
}

path = best_first_search(graph, heuristic, 'A', 'G')
print("Best First Search Path:", path)
