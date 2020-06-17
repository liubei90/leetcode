#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (42.12%)
# Likes:    523
# Dislikes: 0
# Total Accepted:    95.8K
# Total Submissions: 227.4K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
# 
# 示例 1:
# 
# 输入: 1->2
# 输出: false
# 
# 示例 2:
# 
# 输入: 1->2->2->1
# 输出: true
# 
# 
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        c = head
        p = c.next
        while p:
            n = p.next
            p.next = c
            c = p
            p = n

        head.next = None
        return c

    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        fp = head
        sp = head
        while fp:
            fp = fp.next.next if fp.next is not None else None
            if fp:
                sp = sp.next if sp.next is not None else sp

        nexthead = sp.next
        if not nexthead:
            return True

        tailp = self.reverseList(nexthead)
        oldtailp = tailp
        headp = head


        while tailp:
            if headp.val != tailp.val:
                return False

            headp = headp.next
            tailp = tailp.next
        
        sp.next = self.reverseList(oldtailp)
        return True


# @lc code=end

