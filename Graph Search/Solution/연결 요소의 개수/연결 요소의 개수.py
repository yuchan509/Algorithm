from collections import defaultdict, deque

n, m = map(int, input().split())
d = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

visited = [0] * (n + 1)

def bfs(node):
    
    q = deque()
    q.append(node)

    while q:
        x = q.popleft()
        visited[x] = 1

        for i in d[x]:    
            if not visited[i]:
                q.append(i)
                visited[i] = 1         
    return 1

ans = 0
for idx in  range(1, n + 1):
    if not visited[idx]:
        ans += bfs(idx)

print(ans)


# Run.
'''
output : 2
6 5
1 2
2 5
5 1
3 4
4 6
'''