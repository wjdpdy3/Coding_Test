n = int(input())
data = ['0'] * n
for i in range(n):
    data[i] = list(map(str, input().split()))

cnt = 0


def check():
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'S':
                temp_i = i
                temp_j = j
                temp_i += 1
                while (temp_i < n and data[temp_i][temp_j] != 'S' and data[temp_i][temp_j] != 'O'):
                    if data[temp_i][temp_j] == 'T':
                        return False
                    temp_i += 1
                temp_i = i
                temp_i -= 1
                while (temp_i >= 0 and data[temp_i][temp_j] != 'S' and data[temp_i][temp_j] != 'O'):
                    if data[temp_i][temp_j] == 'T':
                        return False
                    temp_i -= 1
                temp_i = i
                temp_j += 1
                while (temp_j < n and data[temp_i][temp_j] != 'S' and data[temp_i][temp_j] != 'O'):
                    if data[temp_i][temp_j] == 'T':
                        return False
                    temp_j += 1
                temp_j = j
                temp_j -= 1
                while (temp_j >= 0 and data[temp_i][temp_j] != 'S' and data[temp_i][temp_j] != 'O'):
                    if data[temp_i][temp_j] == 'T':
                        return False
                    temp_j -= 1
    return True


def dfs(cnt):
    for i in range(n):
        for j in range(n):
            if cnt == 3:
                if check() == True:
                    return True
            else:
                if data[i][j] == 'X':
                    cnt += 1
                    data[i][j] = 'O'
                    if dfs(cnt)==True:
                        return True
                    data[i][j] = 'X'
                    cnt -= 1
    return False


if dfs(cnt) == True:
    print("YES")
else:
    print("NO")


