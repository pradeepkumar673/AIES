# Implement Sum of 1 to N using recursion.

def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

n = 10
result = sum_recursive(n)
print(f"Sum of 1 to {n} = {result}")

n = 100
result = sum_recursive(n)
print(f"Sum of 1 to {n} = {result}")
