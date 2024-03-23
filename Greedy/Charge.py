# N = 1360원
# 500원, 100원, 50원, 10원으로 거스름돈 최소

def solution(N):
    answer = 0
    coin = [500, 100, 50, 10]
    for i in coin:
        answer += N // i
        N %= i

    return answer

N = 1360
print(solution(N))