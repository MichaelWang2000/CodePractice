#
# @lc app=leetcode.cn id=954 lang=python
#
# [954] 二倍数对数组
#

# @lc code=start
class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        num_map = collections.Counter(arr)
        for num in sorted(num_map, key=abs):
            if num_map[num] > num_map[2 * num]:
                return False
            num_map[2 * num] -= num_map[num]
        return True
# @lc code=end

