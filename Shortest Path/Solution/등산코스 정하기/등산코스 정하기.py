import sys
import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):

    graph = defaultdict(list)

    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))

    def dijkstra(gates, summits):
    
        gates, summits = set(gates), set(summits)
        
        q = []
        ans = []
        distances = {node : sys.maxsize for node in graph}

        for gate in gates:
            heapq.heappush(q, (0, gate))

        while q:
            intensity, node = heapq.heappop(q)

            if distances[node] <= intensity : continue
            distances[node] = intensity

            if node in summits: continue

            for next, w in graph[node]:
                new_intensity = max(intensity, w)

                if new_intensity < distances[next]:
                    heapq.heappush(q, (new_intensity, next))

        for summit in summits:
            ans.append([summit, distances[summit]])

        ans.sort(key = lambda x: (x[-1], x[0]))

        return ans[0]

    return dijkstra(gates, summits)


# Run.
'''
output : [5, 3]
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]
'''