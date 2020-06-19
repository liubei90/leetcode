#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (64.02%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    40.4K
# Total Submissions: 63.1K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 输入:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        path = []
        self._dpf(res, path, root)

        return res

    def _dpf(self, res: List[str], path: List[str], node: TreeNode):
        if not node:
            return

        path.append(str(node.val))
        if not node.left and not node.right:
            res.append('->'.join(path))
            path.pop()
            return

        if node.left:
            self._dpf(res, path, node.left)

        if node.right:
            self._dpf(res, path, node.right)

        path.pop()

# @lc code=end

