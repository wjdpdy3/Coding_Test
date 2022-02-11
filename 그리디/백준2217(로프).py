# https://www.acmicpc.net/problem/2217

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
ropes.sort(reverse=True)
result = 0
for k in range(0,n): # 로프를 k개 선택
    result = max(result, ropes[k]*(k+1))
print(result)
