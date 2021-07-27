'''
Author: liubei
Date: 2021-07-23 14:31:46
LastEditTime: 2021-07-23 16:10:25
Description: 
'''
#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#
# https://leetcode-cn.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (51.76%)
# Likes:    145
# Dislikes: 0
# Total Accepted:    23.3K
# Total Submissions: 44.9K
# Testcase Example:  '2'
#
# 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。
# 
# 示例:
# 
# 输入: 2
# 输出: 91 
# 解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
# 
# 
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # dp[i] = dp[i-1]*10 + (9*pow(10, i-2) - dp[i-1])*(i-1);
        # dp = [0, 0,]
        dp = {
            '0': 0,
            '1': 0,
        }

        for i in range(2, n + 1):
            dp[str(i)] = dp[str(i - 1)] * 10 + (9 * pow(10, i - 2) - dp[str(i - 1)]) * (i - 1)

        sum = 0

        for s in dp:
            sum += dp[s]

        return pow(10, n) - sum

    # def countNumbersWithUniqueDigits(self, n: int) -> int:
    #     count = 0
    #     combin = []

    #     def dfs(cn):
    #         nonlocal count

    #         if cn <= 0:
    #             count += 1
    #             # print(combin)
    #             return

    #         for i in range(10):
    #             # 存在重复的数字，直接返回。剪枝
    #             if i in combin:
    #                 continue

    #             if i > 0 or len(combin) > 0:
    #                 combin.append(i)

    #             dfs(cn - 1)

    #             if i > 0 or len(combin) > 0:
    #                 combin.pop()

    #     dfs(n)

    #     return count

    # def countNumbersWithUniqueDigits(self, n: int) -> int:
    #     count = 0

    #     def match(x):
    #         x = list(str(x))
    #         sx = set(x)

    #         return True if len(x) == len(sx) else False

    #     n_max = pow(10, n)

    #     for i in range(n_max):
    #         if match(i):
    #             count += 1

    #     return count
# @lc code=end

# s = Solution()
# s.countNumbersWithUniqueDigits(2)

