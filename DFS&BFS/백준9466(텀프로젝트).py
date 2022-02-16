# https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(10**6)
T = int(input())


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    num = graph[x]

    if visited[num]:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    else:
        dfs(num)

# 2<= n <= 100,000
for _ in range(T):
    n = int(input())
    graph = [0] * (n + 1)
    graph = [0]+ list(map(int, input().split()))
    visited = [True] + [False] * n
    result = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))
