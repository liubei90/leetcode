'''
Author: liubei
Date: 2021-07-20 16:24:54
LastEditTime: 2021-07-20 17:06:01
Description: 
'''
#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (72.44%)
# Likes:    776
# Dislikes: 0
# Total Accepted:    118.9K
# Total Submissions: 164.1K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 
# 回文串 是正着读和反着读都一样的字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 
# 
# 示例 2：
# 
# 
# 输入：s = "a"
# 输出：[["a"]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        combin = []

        def checkCircle(cs):
            st = 0
            ed = len(cs)

            for i in range(len(cs) // 2):
                if cs[st + i] != cs[ed - i - 1]:
                    return False

            return True

        def dfs(s):
            if len(s) <= 0:
                if len(combin) > 0:
                    res.append(combin[:])
                return

            s_len = len(s)

            for i in range(1, s_len + 1):
                if checkCircle(s[0:i]):
                    combin.append(s[0:i])
                    dfs(s[i:])
                    combin.pop()
                # else:
                #     return

        dfs(s)

        return res
# @lc code=end

