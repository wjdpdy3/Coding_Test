import heapq
import sys
def input():
    return sys.stdin.readline().rstrip()

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
trace = [[] for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

start ,end = map(int, input().split())

trace[start].append(start)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                trace[i[0]] = []
                for t in trace[now]:
                    trace[i[0]].append(t)
                trace[i[0]].append(i[0])
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[end])
print(len(trace[end]))
print(' '.join(map(str, trace[end])))


