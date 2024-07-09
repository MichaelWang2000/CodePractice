#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_int = int(a)
        b_int = int(b)
        add = a_int + b_int
        add = str(add)
        added = 0
        final = ''
        for i in range(len(add),0,-1):
            string_i = add[i-1]
            if int(string_i)+added > 1:
                final += str(int(string_i)+added-2)
                added = 1
            else:
                final += str(int(string_i)+added)
                added = 0
        if added != 0:
            final += '1'
        return final[::-1]

# @lc code=end

