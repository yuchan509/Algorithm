def solution(park, routes):

    direction = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

    n, m = len(park), len(park[0])
    x, y = [[i, j] for j in range(m) for i in range(n) if park[i][j] == "S"][0]

    for route in routes:
        op, cnt = route.split()

        nx, ny = x, y
        dx, dy = direction[op]

        for _ in range(int(cnt)):
            nx += dx
            ny += dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m or park[nx][ny] == "X":
                break
        else:
            x, y = nx, ny


    return [x, y]


'''
output : [2, 1]
park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]
'''
