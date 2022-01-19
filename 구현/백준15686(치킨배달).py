from itertools import combinations

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

house = list()
chicken = list()

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            house.append((i+1,j+1))
        if data[i][j] == 2:
            chicken.append((i+1,j+1))

chicken_combination = list(combinations(chicken,m))

# 치킨 거리의 합을 계산
def get_sum(chick):
    result = 0
    for hx, hy in house:
        temp=1e9
        for cx,cy in chick:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result+=temp
    return result

result = 1e9
for chick in chicken_combination:
    result = min(result, get_sum(chick))
print(result)




