#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (51.10%)
# Likes:    1988
# Dislikes: 0
# Total Accepted:    240.2K
# Total Submissions: 469.7K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#

from typing import List

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = -float('inf')
        c = 0
        for i in nums:
            c += i
            if c > m:
                m = c
            if c < 1:
                c = 0
        return m
# @lc code=end

# a = [-2,1,-3,4,-1,2,1,-5,4]
# a = [-2,-3,-1,-5]
# s = Solution()
# n = s.maxSubArray(a)
# print(n)
