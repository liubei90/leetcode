#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
# https://leetcode-cn.com/problems/heaters/description/
#
# algorithms
# Easy (30.34%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 38.8K
# Testcase Example:  '[1,2,3]\n[2]'
#
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
# 
# 现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
# 
# 所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
# 
# 说明:
# 
# 
# 给出的房屋和供暖器的数目是非负数且不会超过 25000。
# 给出的房屋和供暖器的位置均是非负数且不会超过10^9。
# 只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
# 所有供暖器都遵循你的半径标准，加热的半径也一样。
# 
# 
# 示例 1:
# 
# 
# 输入: [1,2,3],[2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
# 
# 
# 示例 2:
# 
# 
# 输入: [1,2,3,4],[1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = float('-inf')

        for h in houses:
            index = -1
            l, r = 0, len(heaters) - 1
            while l <= r:
                m = (l + r) // 2

                index = m
                hm = heaters[m]
                if hm > h and (m == 0 or abs(hm - h) > abs(heaters[m - 1] - h)):
                    r = m - 1
                elif hm < h and (m == len(heaters) - 1 or abs(hm - h) > abs(heaters[m + 1] - h)):
                    l = m + 1
                else:
                    break

            # print(index)

            res = max(res, abs(heaters[index] - h))

        return res

    # def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    #     houses.sort()
    #     heaters.sort()
    #     res = float('-inf')

    #     for h in houses:
    #         index = 0
    #         # 查找最近距离超时
    #         for i in range(len(heaters) - 1):
    #             if abs(heaters[i] - h) > abs(heaters[i + 1] - h):
    #                 index = i + 1
    #             else:
    #                 break

    #         res = max(res, abs(heaters[index] - h))

    #     return res

# @lc code=end

s = Solution()
print(s.findRadius([1,2,3,4], [1,4]))
