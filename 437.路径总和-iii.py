#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (55.49%)
# Likes:    492
# Dislikes: 0
# Total Accepted:    43.2K
# Total Submissions: 77.8K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树，它的每个结点都存放着一个整数值。
# 
# 找出路径和等于给定数值的路径总数。
# 
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
# 
# 示例：
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# 返回 3。和等于 8 的路径有:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.scanNode(root, sum)

    def scanNode(self, node: TreeNode, sum: int) -> int:
        if not node:
            return 0

        total = self.pathSumInNode(node, 0, sum)
        tl = self.scanNode(node.left, sum)
        tr = self.scanNode(node.right, sum)

        return total + tl + tr

    def pathSumInNode(self, node: TreeNode, total: int, sum: int) -> int:
        if not node:
            return 0

        c = 0
        total = node.val + total

        if total == sum:
            c = 1
        c += self.pathSumInNode(node.left, total, sum)
        c += self.pathSumInNode(node.right, total, sum)
        
        return c
# @lc code=end

