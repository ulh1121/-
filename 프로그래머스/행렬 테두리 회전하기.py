def solution(rows, columns, queries):
    answer = []

    square = []
    # 행렬 생성
    num = 1
    for k in range(rows):
        square.append(list(range(num, num + columns)))
        num += columns

    # 회전 실행

    for x1, y1, x2, y2 in queries:
        mini = 10e5
        tmp = square[x1 - 1][y2 - 1]
        mini = min(mini, tmp)

        # 상단 가로
        for t in range(y2 - 1, y1 - 1, -1):
            val = square[x1 - 1][t - 1]
            square[x1 - 1][t] = val
            mini = min(val, mini)
        # 좌측 세로
        for t in range(x1 - 1, x2 - 1):
            val = square[t + 1][y1 - 1]
            square[t][y1 - 1] = val
            mini = min(mini, val)
        # 하단 가로
        for t in range(y1 - 1, y2 - 1):
            val = square[x2 - 1][t + 1]
            square[x2 - 1][t] = val
            mini = min(mini, val)
        # 우측 세로
        for t in range(x2 - 1, x1 - 1, -1):
            val = square[t - 1][y2 - 1]
            square[t][y2-1] = val
            mini = min(mini, val)
        # 미리 저장해둔 값 넣어주기
        square[x1][y2 - 1] = tmp
        # for i in range(len(square)):
        #     print(square[i])

        answer.append(mini)
    return answer
print(solution(6,6,[[2,2,5,4]]))