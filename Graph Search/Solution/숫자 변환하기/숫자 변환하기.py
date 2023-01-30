from collections import deque

def solution(x, y, n):

    v = set()
    q = deque([[x, 0]])

    while q:
        x, cnt = q.popleft()

        if x == y:
            return cnt

        for nx in [x + n, x * 2, x * 3]:
            if nx not in v and nx <= y:
                v.add(nx)
                q.append([nx, cnt + 1])
    return -1

'''
output : 2
x = 10
y = 40
n = 5
'''