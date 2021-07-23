'''
Author: liubei
Date: 2021-07-23 10:52:55
LastEditTime: 2021-07-23 11:20:55
Description: 
'''
#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#
# https://leetcode-cn.com/problems/additive-number/description/
#
# algorithms
# Medium (33.58%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    15.3K
# Total Submissions: 45.7K
# Testcase Example:  '"112358"'
#
# 累加数是一个字符串，组成它的数字可以形成累加序列。
# 
# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
# 
# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
# 
# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
# 
# 示例 1:
# 
# 输入: "112358"
# 输出: true 
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 
# 
# 示例 2:
# 
# 输入: "199100199"
# 输出: true 
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
# 
# 进阶:
# 你如何处理一个溢出的过大的整数输入?
# 
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(numstr, f, s):
            num_len = len(numstr)
            max_len = max(len(f), len(s))

            # 能将字符串分割到空，说明前边的步骤都是正确的
            if num_len == 0:
                return True

            t = numstr[0:max_len]

            if int(f) + int(s) == int(t):
                    return dfs(numstr[max_len:], s, t)

            t = numstr[0:max_len + 1]

            if int(f) + int(s) == int(t):
                    return dfs(numstr[max_len + 1:], s, t)

        num_len = len(num)

        for i in range(1, num_len):
            f = num[0:i]

            for j in range(i, num_len):
                s = num[i:j]

                if dfs(num[j:], f, s):
                    return True

        return False

# @lc code=end

