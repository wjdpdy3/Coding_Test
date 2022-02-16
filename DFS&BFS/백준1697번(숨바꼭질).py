# https://www.acmicpc.net/problem/1697

# n: 수빈, k: 동생
# 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 0 <= n,k <= 100,000

from collections import deque

def location(x, i):
    if i == 0:
        return x + 1
    if i == 1:
        return x - 1
    if i == 2:
        return x * 2

def bfs(x):
    q = deque([x])
    graph[x] = 1

    while q:
        v = q.popleft()
        if v == k:
            return graph[v]
        for i in range(3):
            nx = location(v, i)
            if 0 <= nx <= 100000 and graph[nx] == 0:
                graph[nx] = graph[v] + 1
                q.append(nx)


n, k = map(int, input().split())
graph = [0] * 100001
print(bfs(n) - 1)
