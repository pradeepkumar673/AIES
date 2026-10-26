# Solve the Water Jug Problem.

from collections import deque

def water_jug(capacity_a, capacity_b, target):
    visited = set()
    queue = deque()
    queue.append((0, 0, []))

    while queue:
        a, b, path = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        path = path + [(a, b)]
        if a == target or b == target:
            return path
        states = [
            (capacity_a, b),
            (a, capacity_b),
            (0, b),
            (a, 0),
            (a - min(a, capacity_b - b), b + min(a, capacity_b - b)),
            (a + min(b, capacity_a - a), b - min(b, capacity_a - a)),
        ]
        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))
    return []

solution = water_jug(4, 3, 2)
print("Water Jug Solution Steps:")
for step in solution:
    print(f"  Jug A: {step[0]}L, Jug B: {step[1]}L")
