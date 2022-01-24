# 2차원 리스트(행렬) 90도 회전
def rotate_matrix_90_degree(a):
    row = len(a)
    col = len(a[0])

    res = [[0] * row for _ in range(col)]
    for r in range(row):
        for c in range(col):
            res[c][row - 1 - r] = a[r][c]

    return res

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(rotate_matrix_90_degree(a))
