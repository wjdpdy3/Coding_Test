import copy
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
# 4x4 크기의 정사각형에 존재하는 각 물고기의 번호
array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        # 각 위치마다 [물고기 번호, 방향]을 저장
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

# 8가지 방향에 대한 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


# 현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    return (direction + 1) % 8


result = 0  # 최종 결과


# 현재 배열에서 특정한 번호의 물고기 위치 찾기
# 없으면 None 반환
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None


# 모든 물고기를 회전 및 이동
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 확인
    for i in range(1, 17):
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동 가능한지 확인
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 해당 방향으로 이동 가능하면 이동시키기기
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = turn_left(direction)


# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    # 현재의 방향으로 계속 이동
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 벙위 확인
        if 0 <= now_x < 4 and 0 <= now_y < 4:
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions


# 모든 경우를 탐색하기 위한 DFS
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)  # 리스트를 통째로 복사

    total += array[now_x][now_y][0]  # 현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1  # 물고기를 먹었으므로 번호 값을 -1로 변환

    move_all_fishes(array, now_x, now_y)  # 전체 물고기 이동

    # 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = get_possible_positions(array, now_x, now_y)
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        result = max(result, total)  # 최댓값 저장
        return
    # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)


# 청소년 상어의 시작 위치에서부터 재귀적으로 모든 경우 탐색
dfs(array, 0, 0, 0)
print(result)
