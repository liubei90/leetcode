'''
Author: liubei
Date: 2021-07-06 15:07:30
LastEditTime: 2021-07-06 16:12:36
Description: 
'''
#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (76.89%)
# Likes:    614
# Dislikes: 0
# Total Accepted:    179.2K
# Total Submissions: 233K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#
# c(n,m)=c(n-1,m-1)+c(n-1,m)
# c(2, 1) = c(1, 0) + c(1, 1)

# c(n, 1)*c(n - 1, m - 1)
# n * c(n-1, m-1)

# @lc code=start
class Solution:
    def dfs(self, n, k, pos, combins, ans):
        if len(combins) == k:
            ans.append(combins[:])
            return

        for i in range(pos, n):
            combins.append(i + 1)
            self.dfs(n, k, i + 1, combins, ans)
            combins.remove(i + 1)

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        self.dfs(n, k, 0, [], ans)

        return ans
# @lc code=end

