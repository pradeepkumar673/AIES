# Solve the Monkey and Banana Problem.

from collections import deque

def monkey_banana():
    initial_state = ('door', 'door', 'floor', False)
    goal_state = ('middle', 'middle', 'box', True)

    queue = deque()
    queue.append((initial_state, []))
    visited = set()
    visited.add(initial_state)

    while queue:
        state, actions = queue.popleft()
        monkey_pos, box_pos, monkey_on, has_banana = state

        if has_banana:
            return actions

        next_states = []

        if monkey_pos != 'middle':
            next_states.append(('middle', box_pos, 'floor', False, 'Walk to middle'))
        if monkey_pos != 'door':
            next_states.append(('door', box_pos, 'floor', False, 'Walk to door'))

        if monkey_pos == box_pos and monkey_on == 'floor':
            next_states.append((monkey_pos, box_pos, 'floor', False, f'Push box from {box_pos} to middle') if box_pos != 'middle' else (monkey_pos, 'middle', 'floor', False, 'Push box to middle'))

        if monkey_pos == box_pos and monkey_on == 'floor':
            next_states.append((monkey_pos, box_pos, 'box', False, 'Climb box'))

        if monkey_on == 'box' and monkey_pos == 'middle':
            next_states.append((monkey_pos, box_pos, 'box', True, 'Grab banana'))

        for ns in next_states:
            new_state = ns[:4]
            action = ns[4]
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, actions + [action]))

    return []

solution = monkey_banana()
print("Monkey and Banana Problem Solution:")
for i, action in enumerate(solution, 1):
    print(f"  Step {i}: {action}")
