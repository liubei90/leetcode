'''
Author: liubei
Date: 2021-07-06 10:34:26
LastEditTime: 2021-07-06 10:58:33
Description: 
'''
#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (56.90%)
# Likes:    1383
# Dislikes: 0
# Total Accepted:    291.9K
# Total Submissions: 512.9K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# 示例 2：
# 
# 
# 输入：digits = ""
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：digits = "2"
# 输出：["a","b","c"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# digits[i] 是范围 ['2', '9'] 的一个数字。
# 
# 
#

# @lc code=start
class Solution:
    def dfs(self, digits, idx, dm, combins, ans):
        if idx >= len(digits):
            return

        chars = dm[int(digits[idx])]

        for c in chars:
            newcombins = combins + c

            if idx == len(digits) - 1:
                ans.append(newcombins)

            self.dfs(digits, idx + 1, dm, newcombins, ans)

    def letterCombinations(self, digits):
        dm = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        ans = []

        self.dfs(digits, 0, dm, '', ans)

        return ans
# @lc code=end

s = Solution()
s.letterCombinations('23')
