# Implement Alpha-Beta Pruning.

import math

def alpha_beta(depth, node_index, is_maximizing, scores, height, alpha, beta):
    if depth == height:
        return scores[node_index]
    if is_maximizing:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, False, scores, height, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, node_index * 2 + i, True, scores, height, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

scores = [3, 5, 2, 9, 12, 5, 23, 23]
height = math.log2(len(scores))
result = alpha_beta(0, 0, True, scores, height, -math.inf, math.inf)
print("Alpha-Beta Pruning Optimal Value:", result)
