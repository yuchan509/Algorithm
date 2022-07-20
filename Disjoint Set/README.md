# Algorithm 

## Disjoint Set
|<center>NO|<center>Workbooks|<center>Solution|<center>Memo|
|:---:|:---:|:---:|:---:|
|01|[<center>바이러스](https://www.acmicpc.net/problem/2606)|[<center>바로가기](./Solution/바이러스)||


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
