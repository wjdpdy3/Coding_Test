# https://www.acmicpc.net/problem/1654
import sys
input = sys.stdin.readline

k,n = map(int, input().split())
data = []
for _ in range(k):
    data.append(int(input()))

start = 1
end = max(data)
result = 0
while start<=end:
    mid = (start+end) // 2

    total = 0
    for d in data:
        total += d//mid

    if total < n:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)