n = int(input())
x = 1
y = 1
move = input().split()

# 좌우상하 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for i in move:
    for j in range(len(move_types)):
        if i == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]

# 경계선
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

# 이동
    x, y = nx, ny

print(x, y)