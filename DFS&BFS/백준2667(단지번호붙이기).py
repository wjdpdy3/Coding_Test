# https://www.acmicpc.net/workbook/by/BaaaaaaaaaaarkingDog
# 1:집이 있는곳 / 0:집이 없는곳
# 총 단지수, 집의 수 오름차순 출력
# 5<=n<=25
from collections import deque
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    count = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
                count += 1
                graph[nx][ny] = 0
                q.append((nx,ny))
    return count



result = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            result.append(bfs(i,j))
result.sort()
print(len(result))
for r in result:
    print(r)
