from collections import deque


def solution(maps):
    answer = 0

    for i in range(len(maps)):
        if "S" in maps[i]:
            start = [i, maps[i].index("S")]
            print(start)
        if "L" in maps[i]:
            lever = [i, maps[i].index("L")]

    lever_bfs = bfs(maps, start[0], start[1], "L")
    print(lever_bfs)
    exit_bfs = bfs(maps, lever[0], lever[1], "E")
    print(exit_bfs)

    return lever_bfs + exit_bfs if lever_bfs > -1 and exit_bfs > -1 else -1


def bfs(map, start_x, start_y, target):
    visited = [[False] * len(map[0]) for _ in range(len(map))]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True
    while queue:
        y, x, val = queue.popleft();
        if map[y][x] == target:
            print("dmdm")
            return val
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < len(map) and 0 <= nx < len(map[0]) and map[ny][nx] != "X":
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx, val + 1))

    return -1