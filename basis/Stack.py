# 定义一个栈类  先进后出
class Stack:
    # 初始化
    def __init__(self):
        self.items = []

    # 判断是否为空
    def isEmpty(self):
        return self.items == []

    # 向栈内压入一个元素
    def push(self, item):
        self.items.append(item)

    # 从栈内推出最后一个元素
    def pop(self):
        return self.items.pop()

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)


# 栈属性测试
# s = Stack()
# s.push(7)
# s.push('mira')
# s.push(True)
# print(s.pop())
# print(s.items)
# print(s.size())
# print(s.isEmpty())


# 利用栈将字串的字符反转
def rev_string(my_str):
    stack = Stack()
    out_put = ""
    for i in my_str:
        stack.push(i)
    while not stack.isEmpty():
        out_put += stack.pop()
    return out_put

# test
print(rev_string('qt7mira'))
print(rev_string('12345678'))
print(rev_string('0'))


# 利用栈判断括号平衡Balanced parentheses
def par_checker(par_str):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(par_str) and balanced:
        symbol = par_str[index]
        if symbol in '([{':
            stack.push(symbol)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                balanced = match(stack.pop(), symbol)
        index += 1

    if balanced and stack.isEmpty():
        return True
    else:
        return balanced


def match(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)

# test
print(par_checker('({([(}])}){}'))


# 利用栈实现进制转换
def base_converter(dec_number, base):
    digits = '0123456789ABCDEF'
    stack = Stack()

    while dec_number > 0:
        stack.push(dec_number % base)
        dec_number //= base

    out_put = ''
    print(stack.items)
    while not stack.isEmpty():
        out_put = out_put + digits[stack.pop()]

    return out_put

# test
print(base_converter(170, 16))


def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    stack = Stack()
    postfix_list = []
    token_list= infixexpr.split()

    for token in token_list:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfix_list.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = stack.pop()
        else:
            while (not stack.isEmpty()) and (prec[stack.peek()] >= prec[token]):
                postfix_list.append(stack.pop())
            stack.push(token)
    while not stack.isEmpty():
        postfix_list.append(stack.pop())

    return ''.join(postfix_list)




print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
