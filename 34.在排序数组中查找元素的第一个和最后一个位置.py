'''
Author: liubei
Date: 2021-07-27 09:23:24
LastEditTime: 2021-07-27 09:23:45
Description: 
'''
#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.53%)
# Likes:    1122
# Dislikes: 0
# Total Accepted:    294.9K
# Total Submissions: 693.1K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 
# 进阶：
# 
# 
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 
# 示例 2：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 
# 示例 3：
# 
# 
# 输入：nums = [], target = 0
# 输出：[-1,-1]
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# nums 是一个非递减数组
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = 0
        e = len(nums) - 1
        m = None

        while s <= e:
            m = (s + e) // 2

            if nums[m] == target:
                break

            if nums[m] > target:
                e = m - 1
            else:
                s = m + 1

        if m is not None and nums[m] == target:
            ml = m
            while ml > 0 and nums[ml - 1] == target:
                ml -= 1

            mr = m
            while mr < len(nums) - 1 and nums[mr + 1] == target:
                mr += 1

            return [ml, mr]

        return [-1, -1]


# @lc code=end

