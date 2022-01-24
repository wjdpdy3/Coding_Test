n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = int(1e9)
max_value = -int(1e9)


def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    if i == n-1:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i + 1])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i + 1])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i + 1])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i + 1]))
            div += 1

dfs(0,data[0])

print(max_value)
print(min_value)
