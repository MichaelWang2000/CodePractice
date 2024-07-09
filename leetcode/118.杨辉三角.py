#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            else:
                result_part = []
                for j in range(i+1):
                    if j == 0 or j == i:
                        ad = 1
                    else:
                        ad = result[i-1][j-1] + result[i-1][j]
                    result_part.append(ad)
                result.append(result_part)
        return result
# @lc code=end

