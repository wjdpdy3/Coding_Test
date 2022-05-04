# https://www.acmicpc.net/problem/2805
import sys
from bisect import bisect_right

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start = 0
end = max(trees)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    idx = bisect_right(trees, mid)
    for i in range(idx, n):
        total += trees[i] - mid

    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1


print(result)
