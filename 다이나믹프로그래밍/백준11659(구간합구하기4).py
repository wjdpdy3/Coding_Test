# https://www.acmicpc.net/problem/11659
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

dp_sum = [0] * n
dp_sum[0] = arr[0]
for i in range(1,n):
    dp_sum[i] = dp_sum[i-1] + arr[i]

dp_minus = [0] * n
for i in range(1,n):
    dp_minus[i] = dp_minus[i-1] + arr[i-1]

for _ in range(m):
    i,j = map(int, input().split())
    print(dp_sum[j-1]-dp_minus[i-1])
