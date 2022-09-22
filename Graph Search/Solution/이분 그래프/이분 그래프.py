from collections import deque, defaultdict

def bfs(x):
    q = deque([x])
    visited[x] = 0

    while q:
        x = q.popleft()

        for node in graph[x]:
            if visited[node] == -1:
                visited[node] = (visited[x] + 1) % 2
                q.append(node)

def is_bi():
    for x in range(1, v + 1):
        for j in graph[x]:
            if visited[x] == visited[j]:
                return False
    return True


for _ in range(int(input())):

    graph = defaultdict(list)
    v, e = map(int, input().split())
    visited = [-1] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 비연결 그래프 Case를 위해 완전탐색 수행.
    for i in range(1, v + 1):
        if visited[i] == -1:
            bfs(i)

    if is_bi():
        print("YES")
    else:
        print("NO")


'''
output :
YES
NO

2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
'''