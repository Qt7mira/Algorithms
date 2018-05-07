import numpy as np

line = [[0] * 6] * 5
for i in range(5):
    line[i] = input("请输入第" + str(i) + "行：").split(',')
    # 将line中的元素转换为整型
    line[i] = list(map(int, line[i]))

puzzle = np.array(line)
print(puzzle)
zero = np.zeros(6)
# 向puzzle中的最上面加入一行0
puzzle = np.insert(puzzle, 0, values=zero, axis=0)
# 向puzzle中的最后一列加入一列0
puzzle = np.insert(puzzle, 6, values=zero, axis=1)
# 向puzzle中的第0列加入一行0
puzzle = np.insert(puzzle, 0, values=zero, axis=1)

b = [[0 for col in range(8)] for row in range(6)]  # 6*8  不要写反
press = np.array(b)


def guess():
    print("here count")
    r_len = len(puzzle) - 1
    print(r_len)
    c_len = len(puzzle[0]) - 1
    print(c_len)

    for r in range(1, r_len):
        for c in range(1, c_len):
            press[r + 1][c] = (puzzle[r][c] + press[r][c] + press[r - 1][c] + press[r][c - 1] + press[r][c + 1]) % 2
    for c in range(1, c_len):
        if (press[r_len][c - 1] + press[r_len][c + 1] + press[r_len - 1][c]) % 2 != \
                puzzle[r_len][c]:
            return False
    return True


def enum_f():
    while guess() is False:
        press[1][1] += 1
        c = 1
        while press[1][c] > 1:
            press[1][c] = 0
            c += 1
            press[1][c] += 1
        continue
    # return press


enum_f()
print("灯的初始状态：\n", puzzle[1:6, 1:7])
print("按下结果为：\n", press[1:6, 1:7])
