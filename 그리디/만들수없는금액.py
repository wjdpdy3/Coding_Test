n = int(input())
data = list(map(int,input().split()))

data.sort()

target = 1
for x in data:
    if target<x:
        break
    target+=x

print(target)

# 현재 상태 = '1부터 target-1까지 모든 금액을 만들 수 있는 상태' 
