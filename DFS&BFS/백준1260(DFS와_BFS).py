from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b  = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i = i.sort()

def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)

    visited[start] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

dfs(v)
visited = [False] * (n+1)
print()
bfs(v)
