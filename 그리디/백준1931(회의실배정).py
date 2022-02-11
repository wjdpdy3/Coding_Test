# https://www.acmicpc.net/problem/1931

n = int(input())

data = []
# (시작시간, 끝나는시간)
for _ in range(n):
    data.append(list(map(int, input().split())))
# 끝나는 시간 기준으로 오름차순, 끝나는 시간이 같으면 시작시간 기준으로 오름차순
data.sort(key=lambda x:(x[1],x[0]))

result = 0
cur_time = 0
for start_time, end_time in data:
    if start_time >= cur_time:
        result += 1
        cur_time = end_time
print(result)
