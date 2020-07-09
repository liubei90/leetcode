#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (55.09%)
# Likes:    202
# Dislikes: 0
# Total Accepted:    52.7K
# Total Submissions: 95.6K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
# 
# 注意:
# 假设字符串的长度不会超过 1010。
# 
# 示例 1: 
# 
# 
# 输入:
# "abccccdd"
# 
# 输出:
# 7
# 
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        l = 0
        c_map = {}

        for c in s:
            if c not in c_map:
                c_map[c] = 1
            elif c_map[c] == 0:
                c_map[c] += 1
            elif c_map[c] == 1:
                c_map[c] = 0
                l += 2

        if 1 in c_map.values():
            l += 1

        return l
# @lc code=end

