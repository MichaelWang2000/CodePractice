class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = sum(nums)
        print(right)
        left = 0
        for i in range(len(nums)):
            cur_right =right - nums[i]
            if left == cur_right:
                return i
            left += nums[i]
            right -= nums[i]
        return -1