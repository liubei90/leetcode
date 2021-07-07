'''
Author: liubei
Date: 2021-07-06 11:01:24
LastEditTime: 2021-07-06 13:12:34
Description: 
'''
#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.24%)
# Likes:    1864
# Dislikes: 0
# Total Accepted:    298.1K
# Total Submissions: 385.9K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：["()"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def dfs(self, n, d, combin, rc, ans):
        if d == 0:
            ans.append(combin + rc)
            return

        combin += '('
        rc += ')'
        self.dfs(n, d - 1, combin, rc, ans)

        if d > 1:
            combin += rc
            rc = ''
            self.dfs(n, d - 1, combin, rc, ans)

    def generateParenthesis(self, n):
        ans = []

        self.dfs(n, n, '', '', ans)

        return ans
# @lc code=end

s = Solution()

print(s.generateParenthesis(3))
