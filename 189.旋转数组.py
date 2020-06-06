#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Easy (41.45%)
# Likes:    579
# Dislikes: 0
# Total Accepted:    130K
# Total Submissions: 312.1K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 
# 
# 示例 2:
# 
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 
# 说明:
# 
# 
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        rl = l
        if l < 2:
            return

        def next_i(ci):
            res = (ci + k) % l
            return res

        i = 0
        c = nums[i]
        # 用来判断是否出现循环
        pre_i = i

        while rl > 0:
            rl -= 1
            tmp = c
            i = next_i(i)
            c = nums[i]
            nums[i] = tmp

            # 跳出循环
            if pre_i == i and i + 1 < l:
                i += 1
                c = nums[i]
                pre_i = i

# @lc code=end

# 计算下一个位置，会有循环
# 5 1 5+3 % 7
# 6 2 6+3 % 7


a = [-1,-100,3,99]
s = Solution()
s.rotate(a, 2)
print(a)