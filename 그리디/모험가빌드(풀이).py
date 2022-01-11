n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)

result = 0
i=0
while(i<n):
    result += 1
    i += data[i]

print(result)

