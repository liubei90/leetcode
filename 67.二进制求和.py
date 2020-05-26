#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (52.63%)
# Likes:    367
# Dislikes: 0
# Total Accepted:    83.3K
# Total Submissions: 158.2K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 
# 输入为 非空 字符串且只包含数字 1 和 0。
# 
# 
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
# 
# 
# 提示：
# 
# 
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 是否能使用内置函数？
        return str(bin(int(a, base=2) + int(b, base=2))).replace('0b', '')
# @lc code=end

# b1 = '110'
# b2 = '1'
# s = Solution()
# r = s.addBinary(b1, b2)
# print(r)
