import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


n, m = map(int, input().split())
start = 1
distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

result = distance[2:]
max_distance = max(result)
idx = distance.index(max_distance)
count = result.count(max_distance)
print(f"{idx} {max_distance} {count}")


