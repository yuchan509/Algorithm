import sys
# 재귀 깊이 default : 1000
sys.setrecursionlimit(10 ** 5)

# node class 정의 for 트리 구성
class treeNode:

    # 생성자(Constructor) or 초기화 메서도(init method)
    # >>> class 호출시 반드시 실행되는 부분.
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right= None

class BST:
    # 생성자(Constructor) >> tree root 초기 설정(None)
    def __init__(self) -> None:
        self.root = None
        self.pre  = []
        self.post = []

    def insert(self, node, x):
        # root가 None이라면, self.root = node(x)
        if node is None:
            return treeNode(x)

        # 삽입 값(x) < self.root.data(현재 노드의 값)
        if x < node.data:
            node.left = self.insert(node.left, x)
        # 삽입 값(x) >= self.root.data(현재 노드의 값)
        else:
            node.right = self.insert(node.right, x)

        return node

    def PreOrder(self, node):

        if node is None: return

        self.pre.append(info[node.data])
        self.PreOrder(node.left)
        self.PreOrder(node.right)

    def PostOrder(self, node):

        if node is None: return

        self.PostOrder(node.left)
        self.PostOrder(node.right)
        self.post.append(info[node.data])

def solution(nodeinfo):

    global info
    info = {point[0]: node + 1 for node, point in enumerate(nodeinfo)}
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    bst = BST()
    for x, y in nodeinfo:
        bst.root = bst.insert(bst.root, x)

    bst.PreOrder(bst.root)
    bst.PostOrder(bst.root)
    ans = [bst.pre, bst.post]

    return ans


# Run.
'''
output = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
'''