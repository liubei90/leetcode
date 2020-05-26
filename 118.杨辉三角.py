#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (66.44%)
# Likes:    302
# Dislikes: 0
# Total Accepted:    79.5K
# Total Submissions: 119.6K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        res = [[1]]

        for i in range(1, numRows):
            prer = res[i - 1]
            curr = [1]

            for j in range(1, i):
                curr.append(prer[j - 1] + prer[j])

            curr.append(1)
            res.append(curr)

        return res
# @lc code=end

# s = Solution()
# print(s.generate(5))