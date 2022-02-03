from itertools import *
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

team1_stat = 0
team2_stat = 0
diff = int(1e9)

def calculate_stat(team):
    stat=0
    for i in team:
        for j in team:
            stat += data[i][j]
    return stat

team_list = list(combinations(list(range(n)),n//2))
for team1 in team_list:
    team2 = [i for i in list(range(n)) if i not in team1]
    team1_stat = calculate_stat(team1)
    team2_stat = calculate_stat(team2)
    diff = min(diff, abs(team1_stat - team2_stat))

print(diff)


