import sys
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
print(n,m)
print(graph)

# 입력 확인


def dfs(x, y):
    # 범위 밖 제외
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 방문 처리
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return False
    return False

answer = 0
# 음료 채우기
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1

print(f'answer 는 {answer}')

