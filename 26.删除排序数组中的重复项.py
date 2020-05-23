from typing import List
#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        不能直接在for nums循环中删除nums的元素
        for内部使用了迭代器，next函数通过索引获取下一个元素
        删除i时，原来的i+1就变成了i, 下个循环获取的就是原来i+2的元素，漏了i+1元素的处理
        '''
        o = None
        i = 0
        l = len(nums)
        for _ in range(l):
            c = nums[i]
            if o is not None and o == c:
                nums.pop(i)
                continue
            o = c
            i += 1
        return len(nums)
# @lc code=end

# a = [0,0,1,1,1,2,2,3,3,4]
# s = Solution()
# l = s.removeDuplicates(a)
# print(l, a)