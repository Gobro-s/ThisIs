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
    if x <= 0 or x > n or y < 0 or y >= m:
        return False
    # 방문 처리
    if graph[x][y] == 0:
        graph[x][y] = 1
