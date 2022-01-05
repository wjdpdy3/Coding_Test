n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

result = sorted(data, reverse=True)
for i in range(n):
    print(result[i], end=' ')

