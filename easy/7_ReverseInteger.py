class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = x if x > 0 else -x
        z = 0
        while y > 0:
            z = z * 10 + y % 10
            y = int(y/10)
        # 题目要求:假设我们正在处理一个只能保持32位有符号整数范围内的整数的环境。出于这个问题的目的，假设你的函数在反向整数溢出时返回0。
        if z > pow(2, 31):
            return 0
        z = z if x > 0 else -z
        return z
