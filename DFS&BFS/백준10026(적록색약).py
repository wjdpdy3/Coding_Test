# https://www.acmicpc.net/problem/10026

from collections import deque

# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다
n = int(input())
picture = []
for _ in range(n):
    picture.append(input())
visited = [[False]*n for _ in range(n)]
visited_rg = [[False]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,color):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and picture[nx][ny] == color:
                visited[nx][ny]=True
                q.append((nx,ny))

def bfs_rg(x,y,color):
    q = deque()
    q.append((x,y))
    visited_rg[x][y] = True

    if color == 'R' or color == 'G':
        check = True
    else:
        check = False

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check!=True:
                if 0<=nx<n and 0<=ny<n and visited_rg[nx][ny]==False and picture[nx][ny] == color:
                    visited_rg[nx][ny]=True
                    q.append((nx,ny))
            else:
                if 0 <= nx < n and 0 <= ny < n and visited_rg[nx][ny] == False and picture[nx][ny] !='B':
                    visited_rg[nx][ny] = True
                    q.append((nx, ny))

cnt = 0
cnt_rg = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            color = picture[i][j]
            bfs(i,j,color)
            cnt += 1
        if not visited_rg[i][j]:
            color = picture[i][j]
            bfs_rg(i,j,color)
            cnt_rg += 1

print(cnt, cnt_rg)