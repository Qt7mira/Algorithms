class ListNode:
    """
    ListNode
    """
    def __init__(self, x):
        self.val = x
        self.next = None


def show_linked_list_result(head):
    """
    show_linked_list_result
    :param head:
    :return:
    """
    while head:
        print(head.val)
        head = head.next


def generate_linked_list(list_item):
    """
    generate_linked_list
    :param list_item:
    :return:
    """
    dummy = ListNode(0)
    curr = dummy
    for i in list_item:
        curr.next = ListNode(i)
        curr = curr.next
    return dummy.next


if __name__ == '__main__':

    head_data = [1, 2, 3, 4, 5]
    head = generate_linked_list(head_data)
    show_linked_list_result(head)

