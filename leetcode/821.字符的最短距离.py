#
# @lc app=leetcode.cn id=821 lang=python
#
# [821] 字符的最短距离
#

# @lc code=start
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        # find the location
        result = []
        find_index = []
        len1 = len(s)
        for i in range(len1):
            if s[i] == c:
                find_index.append(i)
        # constrcut the index 
        for i in range(len1):
            if i not in find_index:
                dis = 999
                for j in find_index:
                    if abs(i - j) < dis:
                        dis = abs(i - j)
                result.append(dis)
            else:
                result.append(0)
        
        return result
# @lc code=end
        