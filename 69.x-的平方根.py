#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (38.73%)
# Likes:    399
# Dislikes: 0
# Total Accepted:    153K
# Total Submissions: 395.1K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#

# @lc code=start
class Solution:
    # def mySqrt(self, x: int) -> int:
    #     if x == 0:
    #         return 0

    #     last = 0
    #     res = x
    #     while abs(res - last) < 2:
    #         last = res
    #         res = (res + x / res) // 2

    #     return res

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        err = 0.001
        last = 0
        res = x
        # 趋近结果小于误差结束
        while abs(last - res) > err:
            last = res
            # 牛顿迭代法， 通过x求出x+1的值，不断趋近结果
            res = (res + x / res) / 2

        return int(res)

    def mySqrt2(self, x: int) -> int:
        if x == 0:
            return 0

        last = 0.0
        res = 1.0
        # 精度为系统默认
        while res != last:
            last = res
            res = (res + x / res) / 2

        return res
# @lc code=end

s = Solution()
print(s.mySqrt(8.0))