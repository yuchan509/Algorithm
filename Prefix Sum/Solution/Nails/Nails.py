import sys
input = sys.stdin.readline

n, m = map(int, input().split())
imos = [[0] * (n + 5) for _ in range(n + 5)]

for _ in range(m):
    a, b, x = map(int, input().split())

    imos[a][b] += 1
    imos[a][b + 1] -= 1
    imos[a + x + 1][b] -= 1
    imos[a + x + 1][b + x + 2] += 1
    imos[a + x + 2][b + 1] += 1
    imos[a + x + 2][b + x + 2] -= 1

# left >> right (horizontal)
for r in range(1, n + 3):
    for c in range(1, r + 3):
        imos[r][c] += imos[r][c - 1]

# up >> down (vertical)
for c in range(1, c + 1):
    for r in range(1, n + 3):
        imos[r][c] += imos[r - 1][c]

# left & up >> right & down (diagonal)
for r in range(1, n + 3):
    for c in range(1, r + 3):
        imos[r][c] += imos[r - 1][c - 1]

ans = 0
for r in range(1, n + 3):
    for c in range(1, n + 3):
        if imos[r][c]:
            ans += 1

print(ans)


# run.
'''
output : 12
5 2
2 2 1
2 1 3	
'''
