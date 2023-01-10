# Algorithm 

## Tree
|<center>NO|<center>Workbooks|<center>Solution|<center>Memo|
|:---:|:---:|:---:|:---:|
|01|[ê°??ž¥ ê°?ê¹Œìš´ ê³µí†µ ì¡°ìƒ](https://www.acmicpc.net/problem/3584)|[ë°”ë¡œê°?ê¸?](./Solution/ê°??ž¥%20ê°?ê¹Œìš´%20ê³µí†µ%20ì¡°ìƒ)| |


## BST
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