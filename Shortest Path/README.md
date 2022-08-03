# Algorithm 

## Shortest Path
|<center>NO|<center>Workbooks|<center>Solution|<center>Memo|
|:---:|:---:|:---:|:---:|
|01|[<center>배달](https://school.programmers.co.kr/learn/courses/30/lessons/12978)|[<center>바로가기](./Solution/배달)|  |
|02|[<center>파티](https://www.acmicpc.net/problem/1238)|[<center>바로가기](./Solution/파티)||
|03|[<center>Find the nearest clone](https://www.hackerrank.com/challenges/find-the-nearest-clone/problem)|[<center>바로가기](./Solution/Find%20the%20nearest%20clone)||
|04|[<center>등산코스 정하기](https://school.programmers.co.kr/learn/courses/30/lessons/118669)|[<center>바로가기](./Solution/등산코스%20정하기)||
|05|[<center>택배 배송](https://www.acmicpc.net/problem/5972)|[<center>바로가기](./Solution/택배%20배송)||
|06|[<center>최소비용 구하기](https://www.acmicpc.net/problem/1916)|[<center>바로가기](./Solution/최소비용%20구하기)||
|07|[<center>최단경로](https://www.acmicpc.net/problem/1753)|[<center>바로가기](./Solution/최단경로)||


## Dijkstra's algorithm
- 시작 정점부터 나머지 각 정점까지의 최단거리를 계산하는 알고리즘.
- 어느 간선의 가중치라도 음수가 존재하면 사용 불가능.

### 원리
1. 방문하지 않은 정점 중 가장 가중치 값이 작은 정점을 방문.(처음 : 시작 정점 방문)
2. 해당 정점을 거쳐서 갈 수 있는 정점의 거리가 이전에 기록한 값보다 작다면 그 거리를 갱신.  


```python
import heapq

def dijkstra(graph, start):

    distances = {node : float('inf') for node in graph}
    distances[start] = 0

    q = []
    # (weight, node) 삽입.
    heapq.heappush(q, (distances[start], start))
    
    # 우선 순위 큐가 빌 때까지 반복.
    while q:
        #  가장 작은 가중치를 가진 거리와 노드를 추출.
        dist, now =  heapq.heappop(q)

        if distances[now] < dist: continue

        for adjacent, weight in graph[now]:
            
            # 갱신한 거리 = 기존 거리 + 인접한 노드의 가중치.
            distance = dist + weight
            
            # 갱신한 거리가 배열의 저장된 거리보다 작으면 거리 갱신.
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                # 다음 인접 거리를 계산하기 위해 우선 순위 큐에 삽입 (노드가 동일해도 일단 저장함)
                heapq.heappush(q, [distance, adjacent])

    return distances

```
