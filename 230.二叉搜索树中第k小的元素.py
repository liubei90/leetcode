'''
Author: liubei
Date: 2021-07-28 09:39:37
LastEditTime: 2021-07-28 09:41:32
Description: 
'''
#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (73.64%)
# Likes:    420
# Dislikes: 0
# Total Accepted:    122.4K
# Total Submissions: 165.9K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
# 
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数为 n 。
# 1 
# 0 
# 
# 
# 
# 
# 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        min_val = None
        count = 0

        def dfs(n):
            nonlocal count
            nonlocal min_val

            if min_val:
                return

            if n.left:
                dfs(n.left)

            count += 1

            if count == k:
                min_val = n.val
                return

            if n.right:
                dfs(n.right)

        dfs(root)

        return min_val
# @lc code=end

