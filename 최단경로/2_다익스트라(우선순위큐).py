###############################################################################
# 우선순위 큐 : 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조이다.
# => 여러개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야
# 하는 경우에 우선순위 큐를 이용할 수 있다.

# 힙(Heap) : 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나이다.
# 최소 힙 : 값이 낮은 데이터부터 / 최대 힙 : 값이 높은 데이터부터

#        삽입시간     삭제시간
# 리스트   O(1)        O(N)
# 힙      O(logN)     O(log(N)

###############################################################################
# # 최소 힙
# import heapq
#
# # 오름차순 힙 정렬(Heap Sort)
# def heapsort(iterable):
#     h = []
#     result = []
#     # 모든 원소를 차례대로 힙에 삽입
#     for value in iterable:
#         heapq.heappush(h,value)
#     # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
#     for i in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result
#
# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)

###############################################################################

# # 최대 힙
# import heapq
#
# # 오름차순 힙 정렬(Heap Sort)
# def heapsort(iterable):
#     h = []
#     result = []
#     # 모든 원소를 차례대로 힙에 삽입
#     for value in iterable:
#         heapq.heappush(h,-value)
#     # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
#     for i in range(len(h)):
#         result.append(-heapq.heappop(h))
#     return result
#
# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)

###############################################################################
# < 개선된 다익스트라 알고리즘 >
# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선태갛기 위해 힙(Heap)을 이용.
# 다익스트라 알고리즘이 동작하는 기본 원리는 동일하다.
# -> 현재 가장 가까운 노드를 저장해 놓기 위해 힙 자료구조를 추가적으로 이용한다는 점이 다르다.
# -> 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용한다.

# O(ElogV)
# 노드를 하나씩 검사하는 반복문(while문)은 노드의 개수 V 이상의 횟수로는 처리되지 않는다.
# -> 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수는
#       최대 간선의 개수(E)만큼 연산이 수행될 수 있다.




import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기위한 최단 거리는 0으로 설절하여 큐에 삽입.
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])













