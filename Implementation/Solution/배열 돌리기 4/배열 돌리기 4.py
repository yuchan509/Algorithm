import sys
import copy
from collections import deque
from itertools import permutations

input = sys.stdin.readline

n, m, k = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(n)]
k_arr = [tuple(map(int, input().split())) for _ in range(k)]


def rotate(r, c, s):

    global arr
    r1, r2 = r - s, r + s + 1
    c1, c2 = c - s, c + s + 1

    t = ((2 * s) + 1) // 2

    for _ in range(t):

        temp = [arr[i][c1 : c2] for i in range(r1, r2)]

        R, C = len(temp), len(temp[0])
        left, right, middle = deque(), deque(), deque()

        for row in range(R):
            left.append(temp[row][0])
            right.append(temp[R - row -1][-1])
            rows = deque(temp[row][1 : C - 1])
            middle.append(rows)

        middle[0].appendleft(left.popleft())
        right.append(middle[0].pop())
        middle[-1].append(right.popleft())
        left.append(middle[-1].popleft())

        rot = []
        for _ in range(R):
            rot.append([])
            rot[-1].append(left.popleft())
            rot[-1].extend(list(middle.popleft()))
            rot[-1].append(right.pop())

        for i, j in enumerate(range(r1, r2)):
            arr[j][c1 : c2] = rot[i]

        r1 += 1
        c1 += 1
        r2 -= 1
        c2 -= 1

ans = sys.maxsize
for cases in permutations(k_arr):

    arr = copy.deepcopy(origin)
    for case in cases:
        r, c, s = case
        r -= 1
        c -= 1
        rotate(r, c, s)

    for i in range(n):
        ans = min(ans, sum(arr[i]))

print(ans)

'''
output : 12
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
'''