import sys
from collections import deque, defaultdict

n, k, m = map(int, input().split())
graph = defaultdict(list)

for h in range(1, m + 1):
    arr = list(map(int, sys.stdin.readline().split()))
    for s in arr:
        graph[s].append(n + h)
        graph[n + h].append(s)

def bfs():

    v = set([1])
    q = deque([(1, 0)])

    while q:
        x, cnt = q.popleft()

        if x == n:
            ans = (cnt // 2) + 1
            return ans

        for node in graph[x]:
            if node not in v:
                v.add(node)
                q.append([node, cnt + 1])
    return -1

print(bfs())


'''
output : 4
9 3 5
1 2 3
1 4 5
3 6 7
5 6 7
6 8 9
'''