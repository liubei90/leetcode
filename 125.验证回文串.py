#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (43.61%)
# Likes:    196
# Dislikes: 0
# Total Accepted:    107.5K
# Total Submissions: 244.8K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 示例 1:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "race a car"
# 输出: false
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True

        s_len = len(s)
        l = 0
        r = s_len - 1
        while True:
            l, lv = self._getnext(s, l, 'l')
            r, rv = self._getnext(s, r, 'r')
            if l >= r:
                return True

            if lv.lower() != rv.lower():
                return False
            
            l += 1
            r -= 1

    def _getnext(self, s, i, d):
        c = s[i]
        if c.isalnum():
            return i, c

        s_len = len(s)
        ni = (i + 1) if d == 'l' else (i - 1)
        if ni >= 0 and ni < s_len:
            return self._getnext(s, ni, d)
        
        return ni, None
# @lc code=end

