import sys
input = sys.stdin.readline
MAX = sys.maxsize

n = int(input())

ans = 0
start = end = -MAX

maps = list(tuple(map(int, input().split())) for _ in range(n))
maps.sort()

for a, b in maps:

    if a > end:
        ans += (end - start)
        start = a
        end = b

    if end < b:
        end = b

ans += (end - start)
print(ans)


# Run.
'''
output : 5

4
1 3
2 5
3 5
6 7
'''