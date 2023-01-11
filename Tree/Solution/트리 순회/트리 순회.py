import sys
input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

# ���� ��ȸ(PreOrder) >> root - left - right
def PreOrder(value : str):
    if value.isalpha():
        print(value, end='')
        PreOrder(tree[value][0])  # left
        PreOrder(tree[value][-1]) # right

# ���� ��ȸ(PostOrder) >> left - right - root
def PostOrder(value : str):
    if value.isalpha():
        PostOrder(tree[value][0])  # left
        PostOrder(tree[value][-1]) # right
        print(value, end='')

# ���� ��ȸ(InOrder) >> left - root - right
def InOrder(value : str):
    if value.isalpha():
        InOrder(tree[value][0])  # left
        print(value, end='')
        InOrder(tree[value][-1]) # right

root = 'A'
PreOrder(root)
print()
InOrder(root)
print()
PostOrder(root)


# Run.
'''
output : 
ABDCEFG
DBAECFG
DBEGFCA

7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''