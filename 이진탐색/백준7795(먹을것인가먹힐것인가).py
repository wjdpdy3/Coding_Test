# # https://www.acmicpc.net/problem/7795
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # N:A의수 / M:B의수
    n,m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()

    count = 0
    for a in A:
        right_idx = bisect_right(B,a)
        left_idx = bisect_left(B,a)
        if right_idx - left_idx == 0:
            count += right_idx
        else:
            count += left_idx

    print(count)



