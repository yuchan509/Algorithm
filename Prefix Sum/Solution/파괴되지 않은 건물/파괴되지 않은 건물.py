def solution(board, skill):

    n, m = len(board), len(board[0])
    imos = [[0] * (m + 1) for _ in range(n + 1)]

    for cmd in skill:
        type, r1, c1, r2, c2, degree = cmd

        v = -degree if type == 1 else degree

        imos[r1][c1] += v
        imos[r2 + 1][c2 + 1] += v
        imos[r1][c2 + 1] -= v
        imos[r2 + 1][c1] -= v

    for r in range(n + 1):
        for c in range(1, m + 1):
            imos[r][c] += imos[r][c - 1]

    for c in range(m + 1):
        for r in range(1, n + 1):
            imos[r][c] += imos[r - 1][c]

    ans = 0
    for r in range(n):
        for c in range(m):
            if board[r][c] + imos[r][c] > 0:
                ans += 1

    return ans


# run.
'''
output : 10
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

'''
