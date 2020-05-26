#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (48.60%)
# Likes:    983
# Dislikes: 0
# Total Accepted:    191K
# Total Submissions: 392.6K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        s1 = 1
        s2 = 2
        res = 0
        for _ in range(3, n+1):
            res = s1 + s2
            s1 = s2
            s2 = res
        return res

    # 递归不做缓存的话，执行效率太差
    # def climbStairs(self, n: int) -> int:
    #     if n < 3:
    #         return n
        
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
# @lc code=end

# s = Solution()
# print(s.climbStairs(10))