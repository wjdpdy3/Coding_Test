# https://www.acmicpc.net/problem/10816

from bisect import bisect_left, bisect_right

def range_count(arr, target):
    right_idx = bisect_right(arr, target)
    left_idx = bisect_left(arr, target)
    return right_idx - left_idx

# N:숫자카드의 개수
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
checks = list(map(int, input().split()))

cards.sort()

for check in checks:
    print(range_count(cards, check),end=' ')

