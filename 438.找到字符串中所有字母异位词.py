#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (45.30%)
# Likes:    351
# Dislikes: 0
# Total Accepted:    36.3K
# Total Submissions: 78.9K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
# 
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
# 
# 说明：
# 
# 
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
# 
# 
# 示例 1:
# 
# 
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
# 
# 
# 示例 2:
# 
# 
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
# 
# 
#

from typing import List

# @lc code=start

def all_list(a):
    res = []
    combination(res, a, 0, len(a))
    return res


def combination(res, arr, start, end):
    if start == end:
        res.append(arr[:])

    for i in range(start, end):
        arr[i], arr[start] = arr[start], arr[i]

        combination(res, arr, start + 1, end)

        arr[i], arr[start] = arr[start], arr[i]


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        pa = all_list(list(p))
        pm = { ''.join(i):True for i in pa }
        res = []

        for i in range(0, len(s) - len(p) + 1):
            sub_str = s[i: i+len(p)]
            if sub_str in pm:
                res.append(i)

        return res

# @lc code=end


s = Solution()

print(s.findAnagrams('cbaebabacd', 'abc'))
