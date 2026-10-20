# Write the python program to solve 8-Puzzle problem

import heapq
from itertools import count
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)
def inversion_count(state):
    tiles = [tile for tile in state if tile != 0]
    return sum(
        tiles[first] > tiles[second]
        for first in range(len(tiles))
        for second in range(first + 1, len(tiles))
    )
def manhattan_distance(state):
    distance = 0
    for position, tile in enumerate(state):
        if tile != 0:
            goal_position = tile - 1
            distance += abs(position // 3 - goal_position // 3)
            distance += abs(position % 3 - goal_position % 3)
    return distance
def get_neighbors(state):
    blank_position = state.index(0)
    row, column = divmod(blank_position, 3)
    neighbors = []
    for row_change, column_change in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        next_row = row + row_change
        next_column = column + column_change
        if 0 <= next_row < 3 and 0 <= next_column < 3:
            next_position = next_row * 3 + next_column
            next_state = list(state)
            next_state[blank_position], next_state[next_position] = (
                next_state[next_position],
                next_state[blank_position],
            )
            neighbors.append(tuple(next_state))
    return neighbors
def solve_puzzle(initial_state):
    if inversion_count(initial_state) % 2 != inversion_count(GOAL_STATE) % 2:
        return None
    sequence = count()
    frontier = [(manhattan_distance(initial_state), 0, next(sequence), initial_state)]
    came_from = {initial_state: None}
    cost_so_far = {initial_state: 0}

    while frontier:
        _, current_cost, _, current_state = heapq.heappop(frontier)

        if current_cost != cost_so_far[current_state]:
            continue

        if current_state == GOAL_STATE:
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = came_from[current_state]
            return list(reversed(path))

        for neighbor in get_neighbors(current_state):
            new_cost = current_cost + 1
            if new_cost < cost_so_far.get(neighbor, float("inf")):
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_state
                priority = new_cost + manhattan_distance(neighbor)
                heapq.heappush(frontier, (priority, new_cost, next(sequence), neighbor))

    return None
def display_state(state):
    for row in range(3):
        print(" ".join(str(tile) if tile != 0 else "_" for tile in state[row * 3 : row * 3 + 3]))
    print()
def main():
    try:
        values = tuple(map(int, input("Enter the puzzle row by row, using 0 for the blank: ").split()))
    except ValueError:
        print("Enter exactly the numbers 0 through 8, separated by spaces.")
        return

    if len(values) != 9 or set(values) != set(range(9)):
        print("Enter each number from 0 through 8 exactly once.")
        return

    solution = solve_puzzle(values)
    if solution is None:
        print("This puzzle has no solution.")
        return

    print(f"Solution found in {len(solution) - 1} moves:")
    for move, state in enumerate(solution):
        print(f"Step {move}:")
        display_state(state)


if __name__ == "__main__":
    main()