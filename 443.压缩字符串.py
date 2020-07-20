#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#
# https://leetcode-cn.com/problems/string-compression/description/
#
# algorithms
# Easy (40.13%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    18.3K
# Total Submissions: 45.6K
# Testcase Example:  '["a","a","b","b","c","c","c"]'
#
# 给定一组字符，使用原地算法将其压缩。
# 
# 压缩后的长度必须始终小于或等于原数组长度。
# 
# 数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
# 
# 在完成原地修改输入数组后，返回数组的新长度。
# 
# 
# 
# 进阶：
# 你能否仅使用O(1) 空间解决问题？
# 
# 
# 
# 示例 1：
# 
# 输入：
# ["a","a","b","b","c","c","c"]
# 
# 输出：
# 返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
# 
# 说明：
# "aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
# 
# 
# 示例 2：
# 
# 输入：
# ["a"]
# 
# 输出：
# 返回 1 ，输入数组的前 1 个字符应该是：["a"]
# 
# 解释：
# 没有任何字符串被替代。
# 
# 
# 示例 3：
# 
# 输入：
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# 
# 输出：
# 返回 4 ，输入数组的前4个字符应该是：["a","b","1","2"]。
# 
# 解释：
# 由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
# 注意每个数字在数组中都有它自己的位置。
# 
# 
# 
# 
# 提示：
# 
# 
# 所有字符都有一个ASCII值在[35, 126]区间内。
# 1 <= len(chars) <= 1000。
# 
# 
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        p, c = 0, 0
        cur_c, count = None, 0
        l = len(chars)

        for i in range(l):
            tmp = chars[i]

            if tmp == cur_c:
                count += 1
            else:
                if count > 0:
                    chars[p] = cur_c
                    p += 1
                    if count > 1:
                        for j, s in enumerate(str(count)):
                            chars[p] = s
                            p += 1


                cur_c = tmp
                count = 1

            c = i

        if count > 0:
            chars[p] = cur_c
            p += 1
            if count > 1:
                for j, s in enumerate(str(count)):
                    chars[p] = s
                    p += 1
        return p
# @lc code=end

