#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# https://leetcode-cn.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (47.21%)
# Likes:    201
# Dislikes: 0
# Total Accepted:    40K
# Total Submissions: 84.6K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
# 
# 示例 1:
# 
# 输入: s = "egg", t = "add"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s = "foo", t = "bar"
# 输出: false
# 
# 示例 3:
# 
# 输入: s = "paper", t = "title"
# 输出: true
# 
# 说明:
# 你可以假设 s 和 t 具有相同的长度。
# 
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        l = len(s)

        if len(set(s)) != len(set(t)):
            return False

        for i in range(l):
            c1 = s[i]
            c2 = t[i]
            if c1 in m and m[c1] != c2:
                return False
            m[c1] = c2
        return True
# @lc code=end

