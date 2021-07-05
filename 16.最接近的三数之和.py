'''
Author: liubei
Date: 2021-07-05 17:29:58
LastEditTime: 2021-07-05 18:12:12
Description: 
'''
#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.98%)
# Likes:    814
# Dislikes: 0
# Total Accepted:    229.7K
# Total Submissions: 499.7K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 
# 
# 示例：
# 
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = None
        offset = float('inf')
        nums.sort()
        n = len(nums)

        for f in range(n - 2): # 0 ~ n-3
            fv = nums[f]
            tt = n - 1

            if f == 0 or fv != nums[f - 1]:
                for s in range(f + 1, n - 1): # f+1 ~ n-2
                    sv = nums[s]

                    if s == f + 1 or sv != nums[s - 1]:

                        while s < tt and (fv + sv + nums[tt]) != target and abs((fv + sv + nums[tt]) - target) < offset:
                            offset = abs((fv + sv + nums[tt]) - target)
                            tt -= 1

                        if s < tt:
                            break

                        if (fv + sv + nums[tt]) == target:
                            return target
                        elif not res or abs(res - target) > offset:
                            res = (fv + sv + nums[tt])

        return res
# @lc code=end

