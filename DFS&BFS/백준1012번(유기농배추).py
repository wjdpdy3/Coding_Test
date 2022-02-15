# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10**6)
T = int(input())

# m:가로길이 n:세로길이 k:배추가 심어져있는 위치의 개수
# 배추의 위치(y,x) (가로,세로)
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

for _ in range(T):
    m, n, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                result += 1
    print(result)



