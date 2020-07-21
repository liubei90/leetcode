#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (59.15%)
# Likes:    400
# Dislikes: 0
# Total Accepted:    44.8K
# Total Submissions: 75.7K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
# 
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
# 
# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
# 
# 示例:
# 
# 
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [5,6]
# 
# 
#

# @lc code=start
class Solution:
    '''
    1. 使用hashmap保存出现的数据，空间复杂度为O(n)
    2. 使用二进制保存出现过的数据
    3. 官方通过改变值为负数，通过负数的索引保存出现的数据
    '''
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        tmp = {}
        res = []
        n = len(nums)

        for m in nums:
            if m not in tmp:
                tmp[m] = 1
            else:
                tmp[m] += 1

        for i in range(1, n + 1):
            if i not in tmp:
                res.append(i)

        return res
# @lc code=end

