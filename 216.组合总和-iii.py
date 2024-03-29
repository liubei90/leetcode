'''
Author: liubei
Date: 2021-07-23 10:23:15
LastEditTime: 2021-07-23 10:45:35
Description: 
'''
#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (73.96%)
# Likes:    323
# Dislikes: 0
# Total Accepted:    86.9K
# Total Submissions: 117.4K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 
# 说明：
# 
# 
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 
# 
# 示例 2:
# 
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        combin = []

        # 剪枝
        if n // k > 9:
            return []

        def dfs(rn):
            if rn == 0:
                if len(combin) == k:
                    s = combin[:]
                    s.sort()

                    if s[len(s) - 1] <= 9 and s not in res:
                        res.append(s)

                return

            for i in range(1, rn + 1):
                # 防止重复添加
                if i not in combin:
                    combin.append(i)
                    dfs(rn - i)
                    combin.pop()

        dfs(n)

        return res
# @lc code=end

