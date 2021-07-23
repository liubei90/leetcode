'''
Author: liubei
Date: 2021-07-20 17:10:56
LastEditTime: 2021-07-23 10:16:27
Description: 
'''
#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode-cn.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (48.18%)
# Likes:    260
# Dislikes: 0
# Total Accepted:    26.2K
# Total Submissions: 54.4K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
#  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
# 
# 实现词典类 WordDictionary ：
# 
# 
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些
# '.' ，每个 . 都可以表示任何一个字母。
# 
# 
# 
# 
# 示例：
# 
# 
# 输入：
# 
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
# 
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# addWord 中的 word 由小写英文字母组成
# search 中的 word 由 '.' 或小写英文字母组成
# 最多调用 50000 次 addWord 和 search
# 
# 
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._wd = {}

    def addWord(self, word: str) -> None:
      wd = self._wd

      for i in range(len(word)):
        w = word[i]

        if w not in wd:
          wd[w] = {}

        wd = wd[w]

      wd['_end'] = True

    def search(self, word: str) -> bool:
      return self._search(self._wd, word)

    def _search(self, wd, word):
      # 匹配结束
      if not word:
        return True if '_end' in wd else False

      w = word[0]

      # 单词不在词典中
      if w != '.' and w not in wd:
        return False

      # 单词为.
      if w == '.':
        for k in wd:
          if k == '_end':
            continue

          if self._search(wd[k], word[1:]):
            return True

        return False
      else:
        # 单词匹配上，继续匹配下个单词
        return self._search(wd[w], word[1:])

      # for i in range(len(word)):
      #   w = word[i]

      #   if w in wd:
      #     wd = wd[w]
      #     continue
      #   elif w == '.':
      #     if i == len(word) - 1:
      #       if '_end' in wd:
      #         return True
      #     else:
      #       for k in wd:
      #         if k == '_end':
      #           continue

      #         if self._search(wd[k], word[i + 1:]) == True:
      #           return True

      #   return False

      # return True if '_end' in wd else False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

# ["WordDictionary","addWord","addWord","addWord","addWord",
# "search","search",
# "addWord",
# "search","search","search","search","search","search"]
# ' +
#   '[[],["at"],["and"],["an"],["add"],
#   ["a"],[".at"],
#   ["bat"],
#   [".at"],["an."],["a.d."],["b."],["a.d"],["."]]

# [null,null,null,null,null,
# false,false,
# null,
# true,true,false,false,true,false]

# w = WordDictionary()
# w.addWord('at')
# w.addWord('and')
# w.addWord('an')
# w.addWord('add')

# print(w._wd)

# print(w.search('a'))
# print(w.search('.at'))

# w.addWord('bat')

# print(w._wd)

# print(w.search('.at'))
# print(w.search('an.'))
# print(w.search('a.d.'))
# print(w.search('b.'))
# print(w.search('a.d'))
# print(w.search('.'))
