# Algorithm 

## Disjoint Set
|<center>NO|                             <center>Workbooks                             |         <center>Solution         |<center>Memo|
|:---:|:-------------------------------------------------------------------------:|:--------------------------------:|:---:|
|01|               [바이러스](https://www.acmicpc.net/problem/2606)                |     [바로가기](./Solution/바이러스)      | |
|02| [섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861) |   [바로가기](./Solution/섬%20연결하기)    | |
|03|              [집합의 표현](https://www.acmicpc.net/problem/1717)               |   [바로가기](./Solution/집합의%20표현)    | |
|04| [상근이의 여행](https://school.programmers.co.kr/learn/courses/30/lessons/9372) |   [바로가기](./Solution/상근이의%20여행)   | |
|05|             [최소 스패닝 트리](https://www.acmicpc.net/problem/1197)             | [바로가기](./Solution/최소%20스패닝%20트리) | |
|06|              [사이클 게임](https://www.acmicpc.net/problem/20040)              |   [바로가기](./Solution/사이클%20게임)    | |
|07|               [표 병합](https://school.programmers.co.kr/learn/courses/30/lessons/150366)               |    [바로가기](./Solution/표%20병합)     | |

## Disjoint Set (Union Find)
- 두 집합(Set) 사이에 교집합 원소가 존재하지 않으며(공통으로 포함하는 원소가 없는 두 집합의 관계(서로소(Disjoint))), 모든 집합의 합집합은 전체집합인 자료구조.

    - **Find** : 임의의 원소 x가 주어졌을 때, 이 원소가 속한 집합을 반환.
    - **Union** : 두 집합을 하나의 집합으로 합치는 연산.

        ```python
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]


        def union(a, b):
            a, b = find(a), find(b)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        node, edge = map(int, input().split())

        parent = [i for i in range(1, node + 1)]

        for e in range(edge):
            a, b = map(int, input().split())
            union(a, b)
        ```
