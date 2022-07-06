import heapq
from collections import defaultdict

def solution(N, road, K):

    graph = defaultdict(list)

    for a, b, w in road:
        graph[a].append((b, w))
        graph[b].append((a, w))

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
    for i in dijkstra(graph, 1).values():
        if i <= K:
            ans += 1 

    return ans

    
# Run.
'''
output : 4
N = 5
K = 3
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
'''