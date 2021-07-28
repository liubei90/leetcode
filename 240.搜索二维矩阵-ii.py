'''
Author: liubei
Date: 2021-07-28 09:46:23
LastEditTime: 2021-07-28 09:49:41
Description: 
'''
#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (46.55%)
# Likes:    675
# Dislikes: 0
# Total Accepted:    148.3K
# Total Submissions: 316.4K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
#  '5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 
# 
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -10^9 
# 每行的所有元素从左到右升序排列
# 每列的所有元素从上到下升序排列
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     for m in range(len(matrix)):
    #       m1 = matrix[m]

    #       for n in range(len(m1)):
    #         m2 = m1[n]

    #         if m2 == target:
    #           return True

    #     return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      def match(m1):
        s = 0
        e = len(m1) - 1

        while s <= e:
          m = (s + e) // 2

          if m1[m] == target:
            return True

          if m1[m] > target:
            e = m - 1
          else:
            s = m + 1

        return False

      for i in range(len(matrix)):
        if match(matrix[i]):
          return True

      return False
# @lc code=end

