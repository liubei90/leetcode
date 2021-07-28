'''
Author: liubei
Date: 2021-07-27 11:07:47
LastEditTime: 2021-07-27 11:12:39
Description: 
'''
#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (46.28%)
# Likes:    701
# Dislikes: 0
# Total Accepted:    163.1K
# Total Submissions: 350.6K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr]
# ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 
# 
# 示例 2：
# 
# 
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# 
# 
# 
# 
# 进阶：
# 
# 
# 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
# 
# 
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        e = 0
        count = len(nums) + 1
        total = 0

        for i in range(len(nums)):
            e = i
            total += nums[e]
            if total < target:
                continue
            elif total == target:
                count = min(count, e - s + 1)
            else:
                for j in range(s + 1, e + 1):
                    total -= nums[s]
                    s = j
                    if total > target:
                        continue
                    elif total == target:
                        count = min(count, e - s + 1)
                    else:
                        break

        return count if count != (len(nums) + 1) else 0
# @lc code=end

