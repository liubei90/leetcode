'''
Author: liubei
Date: 2021-07-06 18:01:29
LastEditTime: 2021-07-07 09:54:02
Description: 
'''
#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (45.26%)
# Likes:    948
# Dislikes: 0
# Total Accepted:    188K
# Total Submissions: 415.2K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCCED"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "SEE"
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCB"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == board.length
# n = board[i].length
# 1 
# 1 
# board 和 word 仅由大小写英文字母组成
# 
# 
# 
# 
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
# 
# direction t r b l

# @lc code=start
class Solution:

    def next_index(self, m, n, x, y, direction):
        if direction == 't' and (x - 1 >= 0):
            return x - 1, y
        elif direction == 'r' and (y + 1 < n):
            return x, y + 1
        elif direction == 'b' and (x + 1 < m):
            return x + 1, y
        elif direction == 'l' and (y - 1 >= 0):
            return x, y - 1

        return None, None

    def dfs(self, board, word, visited, m, n, pos, idx, x, y):
        # pos是匹配到的最长长度，
        # x\y是数组下标，
        # direction是上个下标到这个下标的方向
        # 为了防止重复遍历相同的位置，需要额外维护一个与 board 等大的 visited 数组，用于标识每个位置是否被访问过

        # print(board[x][y], word[idx])

        if board[x][y] != word[idx]:
            return False

        if idx == len(word) - 1:
            return True

        visited.add((x, y))

        ism = False
        dirs = ['t', 'r', 'b', 'l']

        for d in dirs:
            nx, ny = self.next_index(m, n, x, y, d)

            if nx is not None and ny is not None and (nx, ny) not in visited:
                ism = self.dfs(board, word, visited, m, n, pos, idx + 1, nx, ny)

                if ism:
                    break

        visited.remove((x, y))

        return ism

    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        visited = set()

        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, visited, m, n, 0, 0, i, j):
                    return True

        return False
# @lc code=end

# s = Solution()
# print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))

