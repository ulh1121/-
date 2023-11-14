from collections import deque


def solution(board):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 0
    r = len(board)  # 가로
    c = len(board[0])  # 세로
    rx, ry = 0, 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                rx, ry = i, j

    def bfs():
        queue = deque()
        queue.append((rx, ry))
        visited = [[0] * c for _ in range(r)]
        visited[rx][ry] = 1

        while queue:
            x, y = queue.popleft()
            if board[x][y] == 'G':
                return visited[x][y]
            for i in range(4):
                nx, ny = x, y
                while True:
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
        return -1

    answer = bfs()
    if answer > 0:
        answer -= 1

    return answer