# 二叉查找（搜索）树是一种把较小数据存储在左节点二较大数据存储在右节点的二叉树。
# 二叉搜索树要求：每个节点都不比它左子树的任意元素小，而且不比它的右子树的任意元素大。


class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self):
        self.root = Node()

    def add(self, elem):

        def add_node(treeNode, elem):

            if elem <= treeNode.elem:
                if treeNode.lchild is None:

                    treeNode.lchild = node
                else:
                    add_node(treeNode.lchild, elem)
            else:
                if treeNode.rchild is None:
                    treeNode.rchild = node
                else:
                    add_node(treeNode.rchild, elem)

        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
        else:
            add_node(self.root, elem)

    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root is None:
            return
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def search(self, elem):
        def search_node(treeNode, elem):
            if elem == treeNode.elem:
                print('success')
                return 'success'
            elif elem < treeNode.elem:
                if treeNode.lchild is None:
                    return
                else:
                    search_node(treeNode.lchild, elem)
            else:
                if treeNode.rchild is None:
                    return
                else:
                    search_node(treeNode.rchild, elem)
        search_node(self.root, elem)

elems = range(10)
tree = Tree()
for elem in elems:
    tree.add(elem)
# tree.front_digui(tree.root)
print(tree.search(8))
print(tree.search(13))





