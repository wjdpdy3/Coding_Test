from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
r, c = map(int, input().split())
board, res = [], 0

F, J = deque(), deque()

for i in range(r):
    data = list(input().rstrip())
    for j in range(c):
        if data[j] == 'J':
            J.append((i, j))
        if data[j] == 'F':
            F.append((i, j))

    board.append(data)


def bfs():
    global F, J, res

    while 1:
        res += 1
        temp = []

        while F:
            x, y = F.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if board[nx][ny] == '.' or board[nx][ny] == '$':
                        temp.append((nx, ny))
                        board[nx][ny] = 'F'
        F = deque(temp)

        temp = []
        while J:
            x, y = J.popleft()
            if x==0 or y==0 or x==r-1 or y==c-1:
                return res

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<r and 0<=ny<c and board[nx][ny] == '.':
                    temp.append((nx, ny))
                    board[x][y] , board[nx][ny] = '$', 'J'

        J = deque(temp)
        if not J:
            return False

if bfs():
    print(res)
else:
    print("IMPOSSIBLE")