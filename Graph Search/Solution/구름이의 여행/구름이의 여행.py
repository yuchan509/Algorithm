import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    
    v = set([1])
    q = deque([[1, 0]])

    while q:
        x, cnt = q.popleft()

        if x == n:
            return "YES" if cnt <= k else "NO"
        
        for node in graph[x]:
            if node not in v:
                v.add(node)
                q.append([node, cnt + 1])
    
    return "NO"

print(bfs())


'''
output : "YES"
6 6 2
1 4
4 2
2 6
4 3
1 2
3 1
'''