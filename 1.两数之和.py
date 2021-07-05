'''
Author: liubei
Date: 2021-07-05 15:25:00
LastEditTime: 2021-07-05 16:03:32
Description: 
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)

        for i, v in enumerate(nums):
            # if v > target:
            #     continue

            for j in range(i + 1, l):
                if v + nums[j] == target:
                    return [i, j]

# @lc code=end

