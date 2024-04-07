n, m = map(int,input().split())

answer = 0
for i in range(n):
    data = list(map(int,input().split()))
    minnum = min(data)
    answer = max(answer, minnum)

print(answer)