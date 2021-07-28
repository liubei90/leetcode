'''
Author: liubei
Date: 2021-07-27 09:46:52
LastEditTime: 2021-07-27 09:47:00
Description: 
'''
#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (37.57%)
# Likes:    694
# Dislikes: 0
# Total Accepted:    200K
# Total Submissions: 531.5K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 
# 
# 示例 2：
# 
# 
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 
# 
# 示例 3：
# 
# 
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# 
# 
# 提示：
# 
# 
# -100.0 
# -2^31 
# -10^4 
# 
# 
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x→x2→x4→x9→x19→x38→x77
        def _pow(n):
            if n == 0:
                return 1

            if n == 1:
                return x

            m = n // 2
            y = _pow(m)

            if n % 2 == 1:
                return y * y * x

            return y * y

        return _pow(n) if n >= 0 else  1/_pow(-n)
# @lc code=end

