# 맵 크기 입력
n,m = map(int, input().split())

# 방문 여부 저장
visited = [[0] * m for _ in range(n)]

# 캐릭터의 현재 x,y 좌표와 방향 입력
x, y, direction = map(int, input().split())
# 입력 받은 현재 좌표는 방문 처리
visited[x][y] = 1

# 전체 맵 정보 입력
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽(반시계 90도)로 회전
def leftturn():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

answer = 1
turn_time = 0
while True:
    leftturn()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 이후 안가본 칸
    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        answer += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 전부 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있는 경우 이동
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다
        else:
            break
        turn_time = 0
print(answer)