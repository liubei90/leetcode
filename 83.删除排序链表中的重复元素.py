#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (50.30%)
# Likes:    310
# Dislikes: 0
# Total Accepted:    100.9K
# Total Submissions: 200.3K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = None
        curr = None
        pp = None
        while True:
            if not curr:
                curr = head
            else:
                curr = curr.next

            # 遍历完成
            if not curr:
                break

            if prev == curr.val:
                pp.next = curr.next
            else:
                prev = curr.val
                pp = curr
        return head

# @lc code=end

