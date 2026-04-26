import heapq

def dijkstra(start, n, adj):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist


def solve():
    # ---------- ЗЧИТУВАННЯ З ФАЙЛУ ----------
    with open("gamsrv.in.txt", "r") as f:
        n, m = map(int, f.readline().split())

        clients = set(map(int, f.readline().split()))

        adj = [[] for _ in range(n + 1)]

        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            adj[u].append((v, w))
            adj[v].append((u, w))

    # ---------- ОБЧИСЛЕННЯ ----------
    best = float('inf')

    for start in range(1, n + 1):
        if start in clients:
            continue

        dist = dijkstra(start, n, adj)

        worst = max(dist[c] for c in clients)
        best = min(best, worst)

    # ---------- ЗАПИС У ФАЙЛ ----------
    with open("gamsrv.out.txt", "w") as f:
        f.write(str(best))


if __name__ == "__main__":
    solve()