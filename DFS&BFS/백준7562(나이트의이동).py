# https://www.acmicpc.net/problem/7562
from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 1

    while q:
        x, y = q.popleft()

        if x == end_x and y == end_y:
            return graph[x][y] - 1
        for l_x, l_y in location:
            nx = x + l_x
            ny = y + l_y

            if 0<=nx<l and 0<=ny<l and graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))



T = int(input())

location = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
for _ in range(T):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    print(bfs(start_x, start_y))
