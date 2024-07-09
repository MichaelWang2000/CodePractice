#
# @lc app=leetcode.cn id=713 lang=python
#
# [713] 乘积小于 K 的子数组
#
import itertools
# @lc code=start
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        nums = [i for i in nums if i < k]
        for i in range(0,len(nums)):
            for j in range(i,len(nums)+1):
                final = 1
                if nums[i:j] == []:
                    continue
                for m in nums[i:j]:
                    final = final * m
                if final < k:
                    # print(nums[i:j])
                    # print(i)
                    # print(j)
                    result += 1
        return result
        
# @lc code=end

