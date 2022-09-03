import heapq
from collections import defaultdict

n, m = map(int, input().split())
start = int(input())

conn = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    conn[a].append((b, w))
    
q = []

def dijkstra(start):
    
    INF = float('inf')
    distance = [INF] * (n + 1)
    
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
    
    ans = ['INF' if i == INF else i for i in distance[1:]]
    return ans 

print(*dijkstra(start), sep = '\n')


# Run.
'''
output : 
0
2
3
7
INF

5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''