'''
Author: liubei
Date: 2021-07-05 16:31:17
LastEditTime: 2021-07-05 17:24:10
Description: 
'''
#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for f in range(n - 2): # 0 ~ n-3
            fv = nums[f]
            tt = n - 1

            if f == 0 or fv != nums[f - 1]:
                for s in range(f + 1, n - 1): # f+1 ~ n-2
                    sv = nums[s]

                    if s == f + 1 or sv != nums[s - 1]:
                        while s < tt and fv + sv + nums[tt] > 0:
                            tt -= 1
                        
                        if s == tt:
                            break

                        if fv + sv + nums[tt] == 0:
                            res.append([fv, sv, nums[tt]])

                        # for t in range(tt, s, -1): # s+1 ~ n-1
                        #     tv = nums[t]

                        #     if fv + sv + tv == 0:
                        #         res.append([fv, sv, tv])
                        #         tt = t - 1
                        #         break

        return res

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     nums.sort()
    #     n = len(nums)

    #     for f in range(n): # 0 ~ n-1
    #         fv = nums[f]

    #         if f == 0 or fv != nums[f - 1]:
    #             for s in range(f + 1, n - 1): # f+1 ~ n-2
    #                 sv = nums[s]

    #                 if s == f + 1 or sv != nums[s - 1]:
    #                     for t in range(s + 1, n): # s+1 ~ n-1
    #                         tv = nums[t]

    #                         if t == s + 1 or tv != nums[t - 1]:
    #                             if fv + sv + tv == 0:
    #                                 res.append([fv, sv, tv])

    #     return res

# @lc code=end

