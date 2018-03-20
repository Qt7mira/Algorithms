class Node(object):
    def __init__(self, elem=-1, lchaild=None, rchild=None):
        self.elem = elem
        self.lchild = lchaild
        self.rchild = rchild


class Tree(object):
    def __init__(self):
        self.root = Node()
        self.myQuene = []

    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQuene.append(self.root)
        else:
            treeNode = self.myQuene[0]
            if treeNode.lchild is None:
                treeNode.lchild = node
                self.myQuene.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQuene.append(treeNode.rchild)
                self.myQuene.pop(0)

    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root is None:
            return
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root is None:
            return
        self.middle_digui(root.lchild)
        print(root.elem)
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root is None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.elem)

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root is None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem)
            if node.lchild is not None:
                myQueue.append(node.lchild)
            if node.rchild is not None:
                myQueue.append(node.rchild)


elems = range(10)
tree = Tree()
for elem in elems:
    tree.add(elem)

# tree.front_digui(tree.root)
# tree.middle_digui(tree.root)
# tree.later_digui(tree.root)
tree.level_queue(tree.root)
