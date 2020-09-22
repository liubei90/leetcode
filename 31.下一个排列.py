#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (34.40%)
# Likes:    668
# Dislikes: 0
# Total Accepted:    90K
# Total Submissions: 260.7K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须原地修改，只允许使用额外常数空间。
# 
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)

        if l < 2:
            return

        for i in range(1, l):
            c = nums[l - i]
            p_c = nums[l - i - 1]

            if p_c < c:
                j = None

                if i == 1:
                    j = l - 1

                for m in range(l - i + 1, l):
                    if p_c < nums[m - 1] and p_c > nums[m]:
                        j = m
                        break

                tmp = nums[l - i - 1]
                nums[l - i - 1] = nums[j]
                nums[j] = tmp

                self.reverse(nums, l - i)
                return

        nums.sort(reverse=True)

    def reverse(self, nums, start):
        end = len(nums) - 1

        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1

# @lc code=end

