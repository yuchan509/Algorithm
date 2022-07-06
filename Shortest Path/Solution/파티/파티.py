import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    
def dijkstra(graph, start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0

    q = []
    heapq.heappush(q, [distances[start], start])
    while q:
        cur_dist, cur_node =  heapq.heappop(q)

        if distances[cur_node] < cur_dist:
            continue

        for adjacent, weight in graph[cur_node]:
            distance = cur_dist + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(q, [distance, adjacent])

    return distances

ans = 0
for node in range(1, n  + 1):
    ans = max(dijkstra(graph, node) [x] + dijkstra(graph, x)[node], ans)

print(ans)


# Run.
'''
output : 10
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''