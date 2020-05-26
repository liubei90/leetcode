#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (44.11%)
# Likes:    467
# Dislikes: 0
# Total Accepted:    153.9K
# Total Submissions: 348.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 
# 
# 示例 2:
# 
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        for i in range(l-1, -1, -1):
            d = digits[i]
            if d + 1 > 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                continue
            digits[i] = d + 1
            break
        return digits
# @lc code=end

ia = [1,2,3]
# ia = [9,9,9]
s = Solution()
print(s.plusOne(ia))
