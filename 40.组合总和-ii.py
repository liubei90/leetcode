'''
Author: liubei
Date: 2021-07-06 13:25:33
LastEditTime: 2021-07-06 13:43:59
Description: 
'''
#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (63.44%)
# Likes:    619
# Dislikes: 0
# Total Accepted:    171K
# Total Submissions: 269.5K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 说明：
# 
# 
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
# 
#

# @lc code=start
class Solution:
    def dfs(self, candidates, idx, target, combins, ans):
        if idx >= len(candidates):
            return

        if target == 0:
            ans.append(combins[:])

        self.dfs(candidates, idx + 1, target, combins, ans)

        if target - candidates[idx] >= 0:
            nc = combins[:]
            nc.append(candidates[idx])
            self.dfs(candidates, idx + 1, target - candidates[idx], nc, ans)

    def combinationSum2(self, candidates, target):
        ans = []

        self.dfs(candidates, 0, target, [], ans)

        return ans
# @lc code=end

s = Solution()
print(s.combinationSum2([2,5,2,1,2], 5))
