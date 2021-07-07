'''
Author: liubei
Date: 2021-07-06 13:59:09
LastEditTime: 2021-07-06 15:02:22
Description: 
'''
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (78.05%)
# Likes:    1430
# Dislikes: 0
# Total Accepted:    351.8K
# Total Submissions: 450.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1]
# 输出：[[1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10 
# nums 中的所有整数 互不相同
# 
# 
#

# @lc code=start
class Solution:
    def dfs(self, nums, place, ans):
        if len(nums) == place:
            ans.append(nums[:])
            return

        for i in range(place, len(nums)):
            nums[i], nums[place] = nums[place], nums[i]
            self.dfs(nums, place + 1, ans)
            nums[i], nums[place] = nums[place], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        self.dfs(nums, 0, ans)

        return ans
# @lc code=end

