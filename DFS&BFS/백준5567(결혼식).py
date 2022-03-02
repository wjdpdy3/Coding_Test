# https://www.acmicpc.net/problem/5567
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
def bfs(start):
    q = deque()
    q.append((start,0))
    visited[start] = True
    result = 0


    while q:
        now, cnt = q.popleft()

        cnt += 1
        for i in graph[now]:
            if not visited[i]:
                if cnt <= 2:
                    result += 1
                visited[i] = True
                q.append((i,cnt))
    return result

print(bfs(1))