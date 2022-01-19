from collections import deque
# 입력값 :
# 노드의수 간선수
# 연결된 간선(A B)
# 연결된 간선(A B)
# ...

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# a->b 간선 존재
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 점에 대한 최단거리 초기화
distance = [-1] * (n + 1)
distance[1] = 0  # 1에서 출발

# 너비 우선 탐색(BFS) 수행
q = deque([1])
while q:
    now = q.popleft()
    print(now,end=' ')
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
