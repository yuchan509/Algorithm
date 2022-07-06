from collections import deque, defaultdict

n, edge = map(int, input().split())

graph = defaultdict(list)

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


color = {idx + 1 : color for idx , color in enumerate(list(map(int, input().split())))}

start = int(input())

def bfs(graph, start):
    
    q = deque()
    q.append([start, 0])

    visited = [0] * (n + 1)
    visited[start] = 1

    while q:
        x, cnt = q.popleft()
        for node in graph[x]:
            if not visited[node]:
                if color[node] == color[start]:
                    return cnt + 1

                visited[node] = 1
                q.append([node, cnt + 1])
    return  -1

print(bfs(graph, start))


# Run.
'''
output : 1
4 3
1 2
1 3
4 2
1 2 1 1 
'''