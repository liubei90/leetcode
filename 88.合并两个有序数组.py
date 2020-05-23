#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (47.61%)
# Likes:    509
# Dislikes: 0
# Total Accepted:    149.7K
# Total Submissions: 313.9K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 
# 
# 
# 说明:
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 
# 
# 示例:
# 
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6]
# 
#

from typing import List

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[p] = nums1[m - 1]
                m -= 1
            else:
                nums1[p] = nums2[n - 1]
                n -= 1
            p -= 1

        if n > 0:
            nums1[0:n] = nums2[0:n]

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        rm = m
        if rm == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        istart = 0
        for i2 in range(n):
            n2 = nums2[i2]
            for i in range(istart, rm):
                c = nums1[i]
                pi = None
                if c >= n2:
                    pi = i
                elif c < n2 and i == rm - 1:
                    pi = rm

                if pi is not None:
                    for l in range(rm - 1, pi - 1, -1):
                        nums1[l + 1] = nums1[l]
                    nums1[pi] = n2
                    rm += 1
                    istart = i
                    break


# @lc code=end

a1 = [1,2,3, 0, 0, 0]
a2 = [2,5,6]
s = Solution()
s.merge(a1, 3, a2, 3)
print(a1)