# 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
#    즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 3. 마지막 도착 계단은 반드시 밟아야 한다.

def calculating_score(n, step): # n : n번째 계단, step : 이전 step 수 (0:1번, 1:2번)
    if n < 0: return 0
    elif dp[n][step]!=0: return dp[n][step] # dp에 값이 존재하면 값을 반환
    elif step==1: # 이전에 2번
        dp[n][step] = scores[n] + max(calculating_score(n-1, 0), calculating_score(n-2, 1))
        return dp[n][step]
    elif step==0: # 이전에 한번
        dp[n][step] += scores[n] + calculating_score(n-2,1)
        return dp[n][step]


n = int(input()) # 계단의 수
scores = [] # 계단 점수
for _ in range(n):
    scores.append(int(input()))

dp = [[scores[0],scores[0]]]
for _ in range(n-1):
    dp.append([0,0])

print(calculating_score(n-1,1))
