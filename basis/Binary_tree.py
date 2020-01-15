class Node(object):
    """
    node
    """
    def __init__(self, val=-1, l_child=None, r_child=None):
        self.val = val
        self.l_child = l_child
        self.r_child = r_child


class Tree(object):
    """
    binary tree
    """
    def __init__(self):
        self.root = Node()
        self.stack = []

    def add(self, val):
        node = Node(val)
        if self.root.val == -1:
            self.root = node
            self.stack.append(self.root)
        else:
            parent_node = self.stack[0]
            if parent_node.l_child is None:
                parent_node.l_child = node
                self.stack.append(parent_node.l_child)
            else:
                parent_node.r_child = node
                self.stack.append(parent_node.r_child)
                self.stack.pop(0)


def front_recursion(root):
    """
    先序遍历 递归
    :param root:
    :return:
    """

    if root is None:
        return

    print(root.val)
    front_recursion(root.l_child)
    front_recursion(root.r_child)


def middle_recursion(root):
    """
    中序遍历 递归
    :param root:
    :return:
    """
    if root is None:
        return
    middle_recursion(root.l_child)
    print(root.val)
    middle_recursion(root.r_child)


def later_recursion(root):
    """
    后序遍历 递归
    :param root:
    :return:
    """
    if root is None:
        return
    later_recursion(root.l_child)
    later_recursion(root.r_child)
    print(root.val)


def level_queue(root):
    """
    层次遍历
    """
    if root is None:
        return
    stack = []
    node = root
    stack.append(node)
    while stack:
        node = stack.pop(0)
        print(node.val)
        if node.l_child is not None:
            stack.append(node.l_child)
        if node.r_child is not None:
            stack.append(node.r_child)


def front_traverse(root):
    """
    前序遍历 非递归
    :param root:
    :return:
    """

    if root is None:
        return

    stack = []
    node = root

    while node or stack:

        # 从根节点开始，一直找它的左子树
        while node:
            print(node.val)
            stack.append(node)
            node = node.l_child

        # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = stack.pop()

        # 开始查看它的右子树
        node = node.r_child


def middle_traverse(root):
    """
    中序遍历 非递归
    :param root:
    :return:
    """

    if root is None:
        return

    stack = []
    node = root

    while node or stack:

        # 从根节点开始，一直找它的左子树
        while node:
            stack.append(node)
            node = node.l_child

        # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = stack.pop()
        print(node.val)

        # 开始查看它的右子树
        node = node.r_child


def last_traverse(root):
    """
    后续遍历 非递归
    :param root:
    :return:
    """

    if root is None:
        return

    stack_1 = []
    stack_2 = []
    node = root

    stack_1.append(node)

    # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
    while stack_1:
        node = stack_1.pop()
        if node.l_child:
            stack_1.append(node.l_child)
        if node.r_child:
            stack_1.append(node.r_child)
        stack_2.append(node)

    while stack_2:
        print(stack_2.pop().val)


if __name__ == '__main__':

    val_list = [1, 2, 3, 4, 5, 6, 7]
    tree = Tree()
    for val in val_list:
        tree.add(val)

    """
        1
     2     3
    4 5   6 7
    """

    front_recursion(tree.root)
    middle_recursion(tree.root)
    later_recursion(tree.root)

    front_traverse(tree.root)
    middle_traverse(tree.root)
    last_traverse(tree.root)

    level_queue(tree.root)
