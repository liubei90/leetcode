#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# https://leetcode-cn.com/problems/happy-number/description/
#
# algorithms
# Easy (60.10%)
# Likes:    362
# Dislikes: 0
# Total Accepted:    81.6K
# Total Submissions: 135.8K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数 n 是不是快乐数。
# 
# 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到
# 1。如果 可以变为  1，那么这个数就是快乐数。
# 
# 如果 n 是快乐数就返回 True ；不是，则返回 False 。
# 
# 
# 
# 示例：
# 
# 输入：19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
#

# @lc code=start
class Solution:
    '''
    类似于快慢指针
    '''
    def isHappy(self, n: int) -> bool:
        f = n
        s = n
        while True:
            f = self._do_happy(f)
            s = self._do_happy(s)
            s = self._do_happy(s)
            if s == f:
                break

        return True if f == 1 else False

    def _do_happy(self, n) -> int:
        res = 0
        while n > 0:
            c = n % 10
            n = n // 10
            res += c * c

        return res
# @lc code=end


# s = Solution()
# print(s.isHappy(19))