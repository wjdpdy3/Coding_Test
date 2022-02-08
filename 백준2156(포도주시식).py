# 1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고,
#    마신 후에는 원래 위치에 다시 놓아야 한다.
# 2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
# 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오.

n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))

dp = [0]
dp.append(wine[1])
if n>1:
    dp.append(wine[1]+wine[2])
for i in range(3,n+1):
    dp.append(max(dp[i-1], dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i] ))
print(dp[n])
