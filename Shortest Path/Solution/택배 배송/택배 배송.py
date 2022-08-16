import sys
import heapq
from collections import defaultdict

n, m = map(int, input().split())

conn = defaultdict(list)

for _ in range(m):
    a, b, w = map(int, input().split())
    conn[a].append((b, w))
    conn[b].append((a, w))

q = []

def dijkstra(start, n):
    
    MAX = 987654321
    distance = {node : MAX for node in conn}
    
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
   
    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist: continue
        
        for next, w in conn[node]:
            new_dist = dist + w
            
            if new_dist < distance[next]:
                distance[next] = new_dist
                heapq.heappush(q, (new_dist, next))
    
    return distance[n]

print(dijkstra(1, n))


# Run.
'''
output : 5
6 8
4 5 3
2 4 0
4 1 4
2 1 1
5 6 1
3 6 2
3 2 6
3 4 4
'''