'''
Author: liubei
Date: 2021-07-26 10:57:42
LastEditTime: 2021-07-26 11:49:30
Description: 
'''
#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# https://leetcode-cn.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (20.61%)
# Likes:    622
# Dislikes: 0
# Total Accepted:    100.3K
# Total Submissions: 485.7K
# Testcase Example:  '10\n3'
#
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) =
# -2
# 
# 
# 
# 示例 1:
# 
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
# 
# 示例 2:
# 
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2
# 
# 
# 
# 提示：
# 
# 
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
# 
# 
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 60/8 = (60-32)/8 + 4 = (60-32-16)/8 + 2 + 4 = 1 + 2 + 4 = 7
        if divisor == 1:
            return dividend
        elif divisor == -1:
            if dividend > -2147483648:
                return -dividend
            else:
                # 处理32位整数溢出
                return 2147483647

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        if abs_dividend < abs_divisor:
            return 0

        count = 1
        c = count
        dd = abs_divisor
        d = dd

        while abs_dividend >= dd:
            c = count
            d = dd
            dd += dd
            count += count

        if abs_dividend - d > 0:
            c += abs(self.divide(abs_dividend - d, abs_divisor))

        return c if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -c
# @lc code=end

s = Solution()
print(s.divide(-2147483648, -1))
# print(s.divide(-2, -1))

