# Algorithm 


## Graph Search
|<center>NO|<center>Workbooks|<center>Solution|<center>Memo|
|:---:|:---:|:---:|:---:|
|01|[<center>게임 맵 최단거리](https://programmers.co.kr/learn/courses/30/lessons/1844)|[<center>바로가기](./Solution/게임%20맵%20최단거리)||
|02|[<center>토마토](https://www.acmicpc.net/problem/7576)|[<center>바로가기](./Solution/토마토)|동시 확산|
|03|[<center>유기농 배추](https://www.acmicpc.net/problem/1012)|[<center>바로가기](./Solution/유기농%20배추)|토마토 유사 문제|
|04|[<center>탈출](https://www.acmicpc.net/problem/3055)|[<center>바로가기](./Solution/탈출)|토마토 확장 사고 문제|
|05|[<center>불!](https://www.acmicpc.net/problem/4179)|[<center>바로가기](./Solution/불!)|탈출 변환 문제| 
|06|[<center>양](https://www.acmicpc.net/problem/3184)|[<center>바로가기](./Solution/양)||
|07|[<center>공주님을 구해라](https://www.acmicpc.net/problem/17836)|[<center>바로가기](./Solution/공주님을%20구해라)|BFS + 조건 만족시 좌표값 거리 계산|
|08|[<center>중량 제한](https://www.acmicpc.net/problem/1939)|[<center>바로가기](./Solution/중량%20제한)|BFS + Binary or MST|
|09|[<center>벽 부수고 이동하기](https://www.acmicpc.net/problem/2206)|[<center>바로가기](./Solution/벽%20부수고%20이동하기)|3D Array 방문 처리|
|10|[<center>미로 탐색](https://www.acmicpc.net/problem/2178)|[<center>바로가기](./Solution/미로%20탐색)||
|11|[<center>경주로 건설](https://programmers.co.kr/learn/courses/30/lessons/67259)|[<center>바로가기](./Solution/경주로%20건설|Coner 처리|
|12|[<center>Count Luck](https://www.hackerrank.com/challenges/count-luck/problem)|[<center>바로가기]|Coner 처리 응용|
|13|[<center>네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162)|[<center>바로가기](./Solution/네트워크)|연결 노드 찾기|
|14|[<center>연결 요소의 개수](https://www.acmicpc.net/problem/11724)|[<center>바로가기](./Solution/연결%20요소의%20개수)|연결 노드 찾기|
|15|[<center>안전 영역](https://www.acmicpc.net/problem/2468)|[<center>바로가기](./Solution/안전%20영역)|Flood Fill|
|16|[<center>단지번호붙이기](https://www.acmicpc.net/problem/2667)|[<center>바로가기](./Solution/단지번호붙이기)|Flood Fill|


## Graph Algorithm
#### 개념
- 그래프는 실제 세계의 현상이나 사물을 정점(Vertex) 또는 노드(Node)와 간선(Edge)로 표현.


#### 종류
- `무방향 그래프(Undirected Graph)` : 두 정점을 연결하는 간선에 방향이 없는 그래프.
- `방향 그래프(Directed Graph)` : 두 정점을 연결하는 간선에 방향이 존재하는 그래프
- `가중치 그래프(Weighted Graph) 또는 네트워크(Network)` : 가중치 그래프는 간선에 가중치(비용)가 할당된 그래프로, 두 정점을 이동할 때 비용이 드는 그래프.
- `연결 그래프(Connected Graph)` : 무방향 그래프에 있는 모든 정점 쌍에 대해서 항상 경로가 존재하는 그래프.
- `비연결 그래프(Disconnected Graph)` : 무방향 그래프에서 특정 정점 사이에 경로가 존재하지 않는 그래프.
- `완전 그래프(Complete graph)` : 그래프의 모든 정점이 서로 연결되어 있는 그래프.
- `순환그래프(Cycle)` : 시작 정점과 도착 정점이 동일한 그래프.
- `비순환그래프(Acyclic Graph)` : 사이클 그래프를 제외한 그래프로, 사이클이 없는 그래프.
- `신장트리(Spanning Tree)` : 원래 그래프의 모든 노드가 연결되어 있으면서, 트리의 속성을 만족하는 그래프.
- `최소 신장트리(Minimum Spanning Tree)` : 신장트리(Spanning Tree)중 간선의 가중치 합이 최소인 신장 트리.


#### 그래프(Graph) 트리(Tree)의 차이
- Tree는 Graph의 한 종류.

    ||<center>Graph|<center>Tree|
    |:---:|:---:|:---:|
    |정의|노드와 노드를 연결하는 간선으로 표현되는 자료구조|그래프의 한 종류로, 방향성이 있는 비순환 그래프|
    |방향성|방향 그래프, 무방향 그래프 둘 다 존재|방향 그래프만 존재|
    |사이킅|사이클이 가능, 순환 및 비순환 그래프 모도 존재|비순환 그래프로 사이클이 존재하지 않음|
    |루트 노드|루트 노드가 존재하지 않음|루트 노드가 존재|
    |부모/자식 관계|부모 자식 개념이 존재하지 않음|부모 자식 관계가 존재|


#### 그래프의 구현 방법
- `인접 리스트(Adjacency List)` : 리스트로 그래프의 연결 관계를 표현하는 방식. 
    - 장점
        - 노드들의 연결 정보를 탐색할 때 $O(n)$ 시간이면 가능.
        - 필요한 만큼의 공간만 사용하므로 공간의 낭비가 적음.
    
    - 단점
        - 구현이 비교적 어려움.
        - 특정 두 점이 연결되었는지 확인하기 위해서는 인접 행렬에 비해 시간이 오래 걸림($O(Edge)$)

- `인접 행렬(Adjacency Matrix)` : 2차원 배열로 그래프의 연결 관계를 표현하는 방식.
    - 장점
        - 구현이 비교적 쉬움.
        - 2차원 배열 안에 모든 정점들의 간선(Edge) 정보를 가지므로 두 정점에 대한 연결 정보의 확인이 빠름($O(1)$)
    
    - 단점
        - 모든 노드에 대한 간선 정보를 대입해야하므로  $O(n^2)$ 시간 복잡도 발생.
        - 무조건 2차원 배열을 필요로하므로 필요 이상의 공간 낭비 발생.
