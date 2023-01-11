# Algorithm 

## Tree
|<center>NO|                  <center>Workbooks                   |           <center>Solution            |<center>Memo|
|:---:|:----------------------------------------------------:|:-------------------------------------:|:---:|
|01|    [트리 순회](https://www.acmicpc.net/problem/1991)     |      [바로가기](./Solution/트리%20순회)       | Tree |
|02| [가장 가까운 공통 조상](https://www.acmicpc.net/problem/3584) | [바로가기](./Solution/가장%20가까운%20공통%20조상) | Lowest Common Ancestor |
|03|    [길 찾기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/42892)     |    [바로가기](./Solution/길%20찾기%20게임)     | Binary Search Tree |
|04|    [잡초 제거](https://level.goorm.io/exam/51351/%EC%9E%A1%EC%B4%88-%EC%A0%9C%EA%B1%B0/quiz/1)     |      [바로가기](./Solution/잡초%20제거)       | Segment Tree|
|05|    [구간합 구하기](https://www.acmicpc.net/problem/2042)     |      [바로가기](./Solution/구간합%20구하기)       | Segment Tree, Fenwick Tree|



## BST(Binary Search Tree)
```python
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        self.curr_node = self.root

        while True:
            if self.curr_node.value > value:
                if self.curr_node.left != None:
                    self.curr_node = self.curr_node.left
                else:
                    self.curr_node.left = node(value)
                    break

            else:
                if self.curr_node.right != None:
                    self.curr_node = self.curr_node.right
                else:
                    self.curr_node.right = node(value)
                    break

    def search(self, value):
        self.curr_node = self.root

        while self.curr_node:
            if self.curr_node.value == value:
                return True

            elif self.curr_node.value > value:
                self.curr_node = self.curr_node.left

            else:
                self.curr_node = self.curr_node.right

        return False
        
 
    root = node(1)
    BST = BinarySearchTree(root)
    BST.insert(2)
    BST.insert(3)
    BST.insert(0)
    BST.insert(4)
    BST.insert(8)

```
