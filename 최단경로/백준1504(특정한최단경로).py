import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

one = dijkstra(1)
v1_d = dijkstra(v1)
v2_d = dijkstra(v2)
result = min(one[v1] + v1_d[v2] + v2_d[n], one[v2]+v2_d[v1]+v1_d[n])
print(result if result < INF else -1)
