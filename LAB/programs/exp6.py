# Implement A* Search Algorithm.

import heapq

def astar(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while priority_queue:
        f, g, node, path = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return g, path
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                g_new = g + weight
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(priority_queue, (f_new, g_new, neighbor, path + [neighbor]))
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

heuristic = {
    'A': 6, 'B': 4, 'C': 5,
    'D': 2, 'E': 3, 'F': 4,
    'G': 0
}

cost, path = astar(graph, heuristic, 'A', 'G')
print("A* Search Path:", path)
print("A* Total Cost:", cost)
