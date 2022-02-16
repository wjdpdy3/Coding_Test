# https://www.acmicpc.net/problem/7576

# 토마토 익을 최소 날짜 출력
# 모두 익어있으면 0 / 모두 익지 못하면 -1
from collections import deque

m,n = map(int, input().split())
graph = []
q = deque([])
for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                q.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1

bfs()
result = 0
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result-1)







