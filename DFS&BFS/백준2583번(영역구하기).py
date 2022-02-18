# https://www.acmicpc.net/problem/2583
from collections import deque
# m:세로, n:가로
m,n,k = map(int, input().split())
graph = [[0]*n for _ in range(m)]

for _ in range(k):
    start_x,start_y,end_x,end_y = map(int, input().split())
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            graph[i][j] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    graph[x][y] = 1
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny]==0:
                graph[nx][ny]=1
                cnt += 1
                q.append((nx,ny))
    return cnt

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(bfs(i,j))
result.sort()
print(len(result))
for r in result:
    print(r, end=' ')