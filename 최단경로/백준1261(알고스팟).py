import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 가로, 세로
m, n = map(int, input().split())
graph = []
distance = [[INF] * m for _ in range(n)]
for _ in range(n):
    graph.append(input())

def dijkstra(start_x, start_y):
    q = []
    heapq.heappush(q, (0, start_x, start_y))
    distance[start_x][start_y] = 0

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == '1':
                    cost = dist + 1
                else:
                    cost = dist
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

dijkstra(0, 0)
print(distance[n-1][m-1])

