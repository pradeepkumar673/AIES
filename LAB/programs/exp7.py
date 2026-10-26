# Implement the Minimax Algorithm.

import math

def minimax(depth, node_index, is_maximizing, scores, height):
    if depth == height:
        return scores[node_index]
    if is_maximizing:
        best = -math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, scores, height)
            best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, scores, height)
            best = min(best, val)
        return best

scores = [3, 5, 2, 9, 12, 5, 23, 23]
height = math.log2(len(scores))
print("Minimax Optimal Value:", minimax(0, 0, True, scores, height))
