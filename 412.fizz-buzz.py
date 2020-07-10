#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode-cn.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (63.95%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    38.4K
# Total Submissions: 60K
# Testcase Example:  '1'
#
# 写一个程序，输出从 1 到 n 数字的字符串表示。
# 
# 1. 如果 n 是3的倍数，输出“Fizz”；
# 
# 2. 如果 n 是5的倍数，输出“Buzz”；
# 
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
# 
# 示例：
# 
# n = 15,
# 
# 返回:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
# 
# 
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        cmap = {
            '3': 'Fizz',
            '5': 'Buzz',
        }
        res = []

        for i in range(1, n + 1):
            c_str = ''
            for c in cmap:
                if i % int(c) == 0:
                    c_str += cmap[c]
            if not c_str:
                c_str = str(i)

            res.append(c_str)

        return res

# @lc code=end

