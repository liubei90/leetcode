#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
# https://leetcode-cn.com/problems/ransom-note/description/
#
# algorithms
# Easy (53.77%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    24.5K
# Total Submissions: 45.6K
# Testcase Example:  '"a"\n"b"'
#
# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines
# 里面的字符构成。如果可以构成，返回 true ；否则返回 false。
# 
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)
# 
# 
# 
# 注意：
# 
# 你可以假设两个字符串均只含有小写字母。
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
# 
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = {}

        for c in ransomNote:
            if c not in ransom_map:
                ransom_map[c] = 1
            else:
                ransom_map[c] += 1
        
        for c in magazine:
            if c in ransom_map:
                ransom_map[c] -= 1

        vals = ransom_map.values()

        return len([n for n in vals if n > 0]) == 0

# @lc code=end

