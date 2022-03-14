import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, -1]

# 전체 테스트 케이스만큼 반복
for tc in range(int(input())):
    n = int(input()) # 노드의 개수
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0 # 시작 위치는 (0,0)
    # 시작 노드로 가기 위한 비용은 (0,0) 위치의 값으로 설정하여 큐에 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
print(distance[n-1][n-1])
