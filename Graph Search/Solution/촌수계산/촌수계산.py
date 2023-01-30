import sys
input = sys.stdin.readline

n, k = map(int, input().split())

l, r = 0, n // 2

while l <= r:
    mid = (l + r) // 2
    y = (mid + 1) * (n - mid + 1)

    if y > k:
        r = mid - 1

    elif y < k:
        l = mid + 1

    else:
        print('YES')
        exit(0)

print('NO')
# Run.
'''
output : 3

9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
'''