# 주어진 수를 M번 더해 가장 큰 수 만들기
# 단 K번 초과해서 더하기 금지
# N = 배열의 크기, M = 더하기 횟수, K

def solution(n, m, k):
    numbers = list(map(int, input().split()))
    numbers.sort()
    first = numbers[-1]
    second = numbers[-2]

    answer = 0

    while True:
        for i in range(k):
            if m == 0:
                break
            else:
                answer += first
                m -= 1
        if m == 0:
            break
        else:
            answer += second
            m -= 1
    return answer
n, m, k = list(map(int, input().split()))
print(solution(n,m,k))