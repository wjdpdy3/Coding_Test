import sys
input = sys.stdin.readline

n, k = map(int, input().split())
multitap = [0] * n
data = list(map(int, input().split()))
result = swap = num = max_l = 0

for i in range(k):
    d = data[i]
    if d in multitap:
        continue
    elif 0 in multitap:
        multitap[multitap.index(0)] = d
    else:
        for m in multitap:
            if m not in data[i:]:
                swap = m
                break
            elif data[i:].index(m) > max_l:
                max_l = data[i:].index(m)
                swap = m
        multitap[multitap.index(swap)] = d
        max_l = swap = 0
        result += 1
print(result)