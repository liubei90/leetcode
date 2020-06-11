#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (45.60%)
# Likes:    395
# Dislikes: 0
# Total Accepted:    81.8K
# Total Submissions: 179.4K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
# 
# 示例:
# 
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        c = head
        p = head.next

        while p:
            if p.val == val:
                c.next = p.next
                p.next = None
                p = c.next
            else:
                c = p
                p = p.next

        return head.next if head.val == val else head



# @lc code=end

