# https://www.acmicpc.net/problem/2606
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
def dfs(x):
    global result

    result += 1
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

dfs(1)

print(result-1)