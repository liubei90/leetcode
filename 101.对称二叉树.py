#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (51.02%)
# Likes:    763
# Dislikes: 0
# Total Accepted:    137K
# Total Submissions: 268.3K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# 进阶：
# 
# 你可以运用递归和迭代两种方法解决这个问题吗？
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
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self._ismirror(root.left, root.right)

    def _ismirror(self, s1, s2):
        if s1 is None and s2 is None:
            return True

        if s1 is None or s2 is None:
            return False
        
        if s1.val != s2.val:
            return False

        return self._ismirror(s1.left, s2.right) and self._ismirror(s1.right, s2.left)

    def isSymmetric2(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self._isSymmetric([root.left], [root.right])
    
    def _isSymmetric(self, sl, sr):
        stackl = []
        stackr = []
        while len(sl) > 0:
            l = sl.pop(len(sl) - 1)
            r = sr.pop(len(sr) - 1)
            if l is None and r is None:
                continue
            elif l is None or r is None:
                return False
            elif l.val != r.val:
                return False
            
            stackl.append(l.left)
            stackl.append(l.right)
            stackr.append(r.right)
            stackr.append(r.left)
        
        if len([l for l in stackl if l is not None]) == 0 and len([r for r in stackr if r is not None]) == 0:
            return True

        return self._isSymmetric(stackl, stackr)
# @lc code=end

