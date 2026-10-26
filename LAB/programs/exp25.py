# Implement Best First Search in Prolog.

import heapq

graph = {
    'a': [('b', 2), ('c', 3)],
    'b': [('d', 4), ('e', 1)],
    'c': [('f', 5)],
    'd': [('goal', 2)],
    'e': [('goal', 3)],
    'f': [('goal', 1)],
    'goal': []
}

heuristic = {
    'a': 6, 'b': 4, 'c': 4,
    'd': 2, 'e': 3, 'f': 1,
    'goal': 0
}

def best_first_search_prolog(graph, heuristic, start, goal):
    open_list = [(heuristic[start], start, [start])]
    closed = set()

    print("Best First Search in Prolog (Python Simulation):")
    print(f"Start: {start}, Goal: {goal}\n")

    while open_list:
        h, current, path = heapq.heappop(open_list)
        print(f"Expanding node: {current} (h={h})")

        if current == goal:
            return path

        if current in closed:
            continue
        closed.add(current)

        for neighbor, _ in graph[current]:
            if neighbor not in closed:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor, path + [neighbor]))

    return []

path = best_first_search_prolog(graph, heuristic, 'a', 'goal')
print("\nPath Found:", path)
