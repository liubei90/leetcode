#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (45.56%)
# Likes:    512
# Dislikes: 0
# Total Accepted:    154.8K
# Total Submissions: 339.8K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self._search_middle(nums, 0, len(nums) - 1, target)

    def _search_middle(self, nums: List[int], l: int, r: int, target: int):
        if l == r:
            if nums[l] >= target:
                return l
            else:
                return l + 1

        if (l + 1) == r:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[l] > target:
                    return l
            elif nums[r] < target:
                    return r + 1
            else:
                return r

        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self._search_middle(nums, m, r, target)
        else:
            return self._search_middle(nums, l, m, target)
# @lc code=end

# a = [1, 2, 5, 6]
a = [1, 3]
o = Solution()
i = o.searchInsert(a, 4)
print(i)