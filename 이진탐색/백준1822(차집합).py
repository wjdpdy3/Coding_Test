from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

def count_by_range(a, left_value, right_value):
    right_idx = bisect_right(a, right_value)
    left_idx = bisect_left(a, left_value)
    return right_idx - left_idx

n_A, n_B = map(int, input().split())
set_A = list(map(int, input().split()))
set_B = list(map(int, input().split()))
set_B.sort()

result = []

for a in set_A:
    if count_by_range(set_B, a, a) == 0:
        result.append(a)

print(len(result))
if result != 0:
    for r in sorted(result):
        print(r, end=' ')