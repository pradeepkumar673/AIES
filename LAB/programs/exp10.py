# Solve the Towers of Hanoi Problem.

def towers_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    towers_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    towers_of_hanoi(n - 1, auxiliary, destination, source)

n = 3
print(f"Towers of Hanoi with {n} disks:")
towers_of_hanoi(n, 'A', 'C', 'B')
