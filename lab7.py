import csv
import math


def read_matrix(islands):
    with open(islands, 'r') as f:
        reader = csv.reader(f)
        matrix = []
        for row in reader:
            matrix.append([float(x) for x in row])
    return matrix


def prim_mst(matrix):
    n = len(matrix)
    visited = [False] * n
    min_edge = [math.inf] * n

    min_edge[0] = 0
    total_cost = 0

    for _ in range(n):
        u = -1

        # вибираємо найближчу вершину
        for i in range(n):
            if not visited[i] and (u == -1 or min_edge[i] < min_edge[u]):
                u = i

        visited[u] = True
        total_cost += min_edge[u]

        # оновлюємо сусідів
        for v in range(n):
            if matrix[u][v] != 0 and not visited[v]:
                min_edge[v] = min(min_edge[v], matrix[u][v])

    return total_cost


matrix = read_matrix("islands.csv")
print("Мінімальна довжина кабелів:", prim_mst(matrix))