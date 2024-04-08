time = int(input())

cnt = 0

# 시
for i in range(time+1):
    # 분
    for j in range(60):
        # 초
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)