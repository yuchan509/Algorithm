# Algorithm 

## Disjoint Set
|<center>NO|<center>Workbooks|<center>Solution|<center>Memo|
|:---:|:---:|:---:|:---:|
|01|[<center>](https://programmers.co.kr/learn/courses/30/lessons/43238)|[<center>�ٷΰ���](./Solution/)||



## Disjoint Set (Union Find)
- �� ����(Set) ���̿� ������ ���Ұ� �������� ������(�������� �����ϴ� ���Ұ� ���� �� ������ ����(���μ�(Disjoint))), ��� ������ �������� ��ü������ �ڷᱸ��.

    - **Find** : ������ ���� x�� �־����� ��, �� ���Ұ� ���� ������ ��ȯ.
    - **Union** : �� ������ �ϳ��� �������� ��ġ�� ����.

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