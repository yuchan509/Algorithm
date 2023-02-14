import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

imos = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    cmd = list(map(int, input().split()))
    op, v = cmd[0], cmd[1:]

    if op == 1:
        r1, c1, r2, c2, k = v
        imos[r1][c1] += k
        imos[r1][c2 + 1] -= k
        imos[r2 + 1][c1] -= k
        imos[r2 + 1][c2 + 1] += k

    else:
        for r in range(n + 1):
            for c in range(1, n + 1):
                imos[r][c] += imos[r][c - 1]

        for c in range(n + 1):
            for r in range(1, n + 1):
                imos[r][c] += imos[r - 1][c]

        ans = 0
        r1, c1, r2, c2 = v
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                ans += arr[r][c] + imos[r][c]

        print(ans)


'''
output : 31

4 3
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 0 0 1 1 1
1 0 0 2 2 2
2 0 0 2 2
'''
