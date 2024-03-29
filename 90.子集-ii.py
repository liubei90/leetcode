'''
Author: liubei
Date: 2021-07-08 09:46:41
LastEditTime: 2021-07-20 13:38:49
Description: 
'''
#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (63.39%)
# Likes:    603
# Dislikes: 0
# Total Accepted:    119.1K
# Total Submissions: 187.9K
# Testcase Example:  '[1,2,2]'
#
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0]
# 输出：[[],[0]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        res = []
        combin = []

        def dfs(idx):
            if idx >= nums_len:
                tmp = combin[:]
                tmp.sort()

                if tmp not in res:
                    res.append(tmp)
                return

            combin.append(nums[idx])
            dfs(idx + 1)

            combin.pop()
            dfs(idx + 1)

        dfs(0)

        return res
# @lc code=end

