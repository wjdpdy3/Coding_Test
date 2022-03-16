def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 집의 수, 도로의 수
n, m = map(int, input().split())
parent = [0] * (n+1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

cost_sum = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    cost_sum += cost

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(cost_sum - result)