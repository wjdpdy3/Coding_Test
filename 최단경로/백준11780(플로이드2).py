import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]
path = [[0] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0
            path[a][b] = [a]


for _ in range(m):
    a,b,c = map(int, input().split())
    # if graph[a][b] != 0:
        # graph[a][b] = min(graph[a][b], c)
    if graph[a][b] !=0:
        if graph[a][b] > c:
            graph[a][b] = c
            path[a][b] = [a,b]

for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            # graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                path[a][b] = path[a][k][:-1] + path[k][b]

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end= " ")
        else:
            print(graph[a][b], end=" ")
    print()

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b or graph[a][b] == INF:
            print(0)
        else:
            print(len(path[a][b]), end=" ")
            print(' '.join(map(str, path[a][b])))