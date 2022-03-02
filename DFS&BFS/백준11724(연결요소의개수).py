# https://www.acmicpc.net/problem/11724
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(a):
    visited[a] = True

    for i in graph[a]:
        if not visited[i]:
            dfs(i)

result = 0
for i in range(1, n+1):
    if not visited[i]:
        result += 1
        dfs(i)

print(result)