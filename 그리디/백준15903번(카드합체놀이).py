# https://www.acmicpc.net/problem/15903

# 1. x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
# 2. 계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.

n ,m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
for _ in range(m):
    s = cards[0] + cards[1]
    cards[0] = s
    cards[1] = s
    cards.sort()
print(sum(cards))
