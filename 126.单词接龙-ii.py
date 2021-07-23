'''
Author: liubei
Date: 2021-07-20 13:53:49
LastEditTime: 2021-07-20 16:22:43
Description: 
'''
#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
# https://leetcode-cn.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (38.96%)
# Likes:    454
# Dislikes: 0
# Total Accepted:    34.2K
# Total Submissions: 87.6K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord ->
# s1 -> s2 -> ... -> sk 这样的单词序列，并满足：
# 
# 
# 
# 
# 每对相邻的单词之间仅有单个字母不同。
# 转换过程中的每个单词 si（1 ）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。
# sk == endWord
# 
# 
# 给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的
# 最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk]
# 的形式返回。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# 输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# 解释：存在 2 种最短的转换序列：
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
# 
# 
# 示例 2：
# 
# 
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# 输出：[]
# 解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# endWord.length == beginWord.length
# 1 
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有单词 互不相同
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        combin = []
        word_len = len(beginWord)
        # wordlist_len = len(wordList)

        def match(pw, cw):
            count = 0

            for i in range(word_len):
                if pw[i] != cw[i]:
                    count += 1

                if count > 1:
                    return False

            return True if count == 1 else False

        def dfs():
            if len(combin) and combin[len(combin) - 1] == endWord:
                res.append(combin[:])
                return

            if len(combin) == 0:
                combin.append(beginWord)

            wordlist_len = len(wordList)

            for w in range(wordlist_len):
                wi = wordList[w]

                if wi not in combin and match(combin[len(combin) - 1], wi):
                    # wordList.remove(wi)
                    combin.append(wi)
                    dfs()
                    # wordList.insert(w, wi)
                    combin.pop()

        dfs()

        shortres = []
        short_len = None

        for item in res:
            item_len = len(item)

            if not short_len or item_len < short_len:
                short_len = item_len
                shortres = [item]
            elif item_len == short_len:
                shortres.append(item)

        return shortres
# @lc code=end

