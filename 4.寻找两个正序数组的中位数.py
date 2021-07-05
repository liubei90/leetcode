'''
Author: liubei
Date: 2021-07-05 16:04:20
LastEditTime: 2021-07-05 16:30:22
Description: 
'''
#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        i1 = 0
        i2 = 0
        l1 = len(nums1)
        l2 = len(nums2)

        e1 = i1 >= l1
        e2 = i2 >= l2

        while True:
            e1 = i1 >= l1
            e2 = i2 >= l2

            if e1 and e2:
                break

            n1 = nums1[i1] if not e1 else 0
            n2 = nums2[i2] if not e2 else 0

            if e1:
                arr.append(n2)
                i2 += 1

            elif e2:
                arr.append(n1)
                i1 += 1
            
            else:
                if n1 > n2:
                    arr.append(n2)
                    i2 += 1
                else:
                    arr.append(n1)
                    i1 += 1

        mi = len(arr) // 2

        return arr[mi] if mi != (len(arr) / 2) else ((arr[mi - 1] + arr[mi]) / 2)

# @lc code=end

