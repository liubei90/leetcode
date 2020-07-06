#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (45.61%)
# Likes:    224
# Dislikes: 0
# Total Accepted:    84.3K
# Total Submissions: 184.7K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 
# 
# 
# 示例：
# 
# s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
# 
# 
# 
# 
# 提示：你可以假定该字符串只包含小写字母。
# 
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_map = {}

        for c in s:
            if c not in s_map:
                s_map[c] = 1
            else:
                s_map[c] += 1

        for i, c in enumerate(s):
            if s_map[c] == 1:
                return i

        return -1
# @lc code=end

