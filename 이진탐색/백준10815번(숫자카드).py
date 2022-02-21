# https://www.acmicpc.net/problem/10815
from bisect import *

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
checks = list(map(int, input().split()))

cards.sort()

for c in checks:
    right_idx = bisect_right(cards, c)
    left_idx = bisect_left(cards,c)
    if right_idx == left_idx:
        print(0, end=' ')
    else:
        print(1, end=' ')


