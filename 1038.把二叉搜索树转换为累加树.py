'''
Author: liubei
Date: 2021-07-23 17:05:42
LastEditTime: 2021-07-26 10:52:37
Description: 
'''
#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 把二叉搜索树转换为累加树
#
# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/description/
#
# algorithms
# Medium (79.18%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    23.1K
# Total Submissions: 29.2K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# 给定一个二叉搜索树，请将它的每个节点的值替换成树中大于或者等于该节点值的所有节点值之和。
# 
# 提醒一下，二叉搜索树满足下列约束条件：
# 
# 
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
# 
# 
# 注意：该题目与 538: https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
# 相同
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 
# 
# 示例 2：
# 
# 
# 输入：root = [0,null,1]
# 输出：[1,null,1]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1,0,2]
# 输出：[3,3,2]
# 
# 
# 示例 4：
# 
# 
# 输入：root = [3,2,4,1]
# 输出：[7,9,4,10]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数介于 1 和 100 之间。
# 每个节点的值介于 0 和 100 之间。
# 树中的所有值 互不相同 。
# 给定的树为二叉搜索树。
# 
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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        groot = TreeNode()
        total = 0

        def loop(r, g):
            nonlocal total

            if r.right:
                gr = TreeNode()
                g.right = gr
                loop(r.right, gr)

            total += r.val
            g.val = total

            if r.left:
                gl = TreeNode()
                g.left = gl
                loop(r.left, gl)

        loop(root, groot)

        return groot
# @lc code=end

