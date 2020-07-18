#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#
# https://leetcode-cn.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (35.61%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    18.9K
# Total Submissions: 53.2K
# Testcase Example:  '"Hello, my name is John"'
#
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
# 
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
# 
# 示例:
# 
# 输入: "Hello, my name is John"
# 输出: 5
# 解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
# 
# 
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        n = 0
        pc = ' '
        for c in s:
            if c != ' ' and pc == ' ':
                n += 1
            pc = c
        return n

# @lc code=end

