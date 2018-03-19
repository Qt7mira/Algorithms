class Solution:
    def isPalindrome(self, x):
        """
        判断x是否是回文
        :type x: int
        :rtype: bool
        
        思路：取后半部分反转后与前半部分比较
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revNumber = 0
        # 原始数字小于倒数时，表示已经处理了一半的数字位数
        while x > revNumber:
            revNumber = revNumber * 10 + x % 10
            x //= 10

        print(revNumber)
        print(x)
        return x == revNumber or x == revNumber // 10

    # 判断字符串是个回文
    def isPalindrome2(self, my_str):
        return my_str == my_str[::-1]

sol = Solution()
print(sol.isPalindrome(1))
print(sol.isPalindrome2('abcde'))
print(sol.isPalindrome2('abcba'))



