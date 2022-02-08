# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은
# A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

n = int(input())
sequence = list(map(int, input().split()))
dp=[0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        # 앞선 숫자들 중에 현재 숫자보다 작고
        # 수열의 길이가 제일 긴 것으로 업데이트.
        if sequence[i]>sequence[j] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i]+=1 # 현재 숫자를 추가함으로 길이에 1 추가
print(max(dp))