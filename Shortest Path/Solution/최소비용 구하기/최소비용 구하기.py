import sys
import heapq
from collections import defaultdict

n = int(input())
m = int(input())

# 정점 간의 간선이 여러개 존재할 수 있으므로 인접리스트로 표현.
conn = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    conn[a].append((b, w))
    
start, end = map(int, input().split())

q = []

def dijkstra(start, end):
    
    MAX = sys.maxsize
    distance = [MAX] * (n + 1)
    
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
    
    return distance[end]

print(dijkstra(start, end))

# Run.
'''
output : 4
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
'''