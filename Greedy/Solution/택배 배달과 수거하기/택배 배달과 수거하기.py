from collections import deque

def solution(cap, n, deliveries, pickups):
    q1 = deque()
    q2 = deque()
    for i, (d, p) in enumerate(zip(deliveries[::-1], pickups[::-1])):
        q1.extend([n - i] * d)
        q2.extend([n - i] * p)

    ans = 0
    while q1 or q2:

        v = max(q1[0] if q1 else 0,
                q2[0] if q2 else 0)

        for _ in range(cap):
            if q1: q1.popleft()
            if q2: q2.popleft()

        ans += v * 2

    return ans


# Run.
'''
output : 16
cap = 4	
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]	
'''