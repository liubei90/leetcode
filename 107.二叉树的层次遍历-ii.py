#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (65.45%)
# Likes:    237
# Dislikes: 0
# Total Accepted:    59.2K
# Total Submissions: 90.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其自底向上的层次遍历为：
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        res = []
        self._colloct_level_data([root], res)
        return res
    
    def _colloct_level_data(self, q, res):
        lres = []
        nlevel = []

        for tn in q:
            if tn is not None:
                lres.append(tn.val)
                nlevel.append(tn.left)
                nlevel.append(tn.right)

        if len(lres):
            res.insert(0, lres)

        if len(nlevel):
            self._colloct_level_data(nlevel, res)

# @lc code=end

