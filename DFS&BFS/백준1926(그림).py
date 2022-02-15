# https://www.acmicpc.net/problem/1926

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    each_cnt = 1
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    each_cnt += 1
    return each_cnt

# 세로, 가로
n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt, max_each_count = 0,0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_each_count = max(max_each_count, bfs(i,j))
print(cnt)
print(max_each_count)
