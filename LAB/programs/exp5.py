# Implement Greedy Best First Search Algorithm.

import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], start, [start])]
    visited = set()

    while priority_queue:
        h, node, path = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))
    return []

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 4)],
    'G': []
}

heuristic = {
    'A': 6, 'B': 4, 'C': 5,
    'D': 2, 'E': 3, 'F': 4,
    'G': 0
}

path = greedy_best_first_search(graph, heuristic, 'A', 'G')
print("Greedy Best First Search Path:", path)
