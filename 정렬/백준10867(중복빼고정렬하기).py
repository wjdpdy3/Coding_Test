n = int(input())
data = list(map(int, input().split()))
array = [0] * 2001

for d in data:
    array[d + 1000] += 1

for i in range(2001):
    if array[i] != 0:
        print(i-1000, end=' ')