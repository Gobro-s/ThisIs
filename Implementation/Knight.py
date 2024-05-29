now = input()
row = int(now[1])
col = int(ord(now[0]))-int(ord('a')) + 1

steps = [(-2,-1), (-2,1), (2,-1), (2,1), (1,2), (1,-2), (-1,-2), (-1,2)]

answer = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        answer += 1

print(answer)