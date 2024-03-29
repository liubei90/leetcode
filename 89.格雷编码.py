'''
Author: liubei
Date: 2021-07-07 14:13:41
LastEditTime: 2021-07-08 09:38:38
Description: 
'''
#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#
# https://leetcode-cn.com/problems/gray-code/description/
#
# algorithms
# Medium (70.76%)
# Likes:    310
# Dislikes: 0
# Total Accepted:    52.6K
# Total Submissions: 74.3K
# Testcase Example:  '2'
#
# 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
# 
# 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。
# 
# 格雷编码序列必须以 0 开头。
# 
# 
# 
# 示例 1:
# 
# 输入: 2
# 输出: [0,1,3,2]
# 解释:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# 
# 对于给定的 n，其格雷编码序列并不唯一。
# 例如，[0,2,3,1] 也是一个有效的格雷编码序列。
# 
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
# 
# 示例 2:
# 
# 输入: 0
# 输出: [0]
# 解释: 我们定义格雷编码序列必须以 0 开头。
# 给定编码总位数为 n 的格雷编码序列，其长度为 2^n。当 n = 0 时，长度为 2^0 = 1。
# 因此，当 n = 0 时，其格雷编码序列为 [0]。
# 
# 
# 00 11

# @lc code=start
class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]

        num = int('1' * n, 2) + 1
        combin = []

        def checked(n1, n2):
            s = format(n1 ^ n2, 'b')
            return s.count('1') == 1

        def dfs():
            cbl = len(combin)

            if cbl == num:
                return True

            for i in range(num):
                if i not in combin and checked(i, combin[cbl - 1]):
                    # 回溯关键代码
                    combin.append(i)

                    # 递归关键代码
                    m = dfs()

                    if m:
                        return True

                    # 回溯关键代码
                    combin.remove(i)

            return False

        combin = [0]

        if dfs():
            print([format(i, 'b') for i in combin])
            return combin

        return []

# @lc code=end


s = Solution()
s.grayCode(3)
