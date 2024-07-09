#
# @lc app=leetcode.cn id=860 lang=python
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        changes = {5:0, 10:0}
        for i in bills:
            if i != 5:
                if i == 10:
                    if changes[5] == 0:
                        return False
                    else:
                        changes[5] -= 1
                        changes[10] += 1
                else:
                    if (changes[5] >0 and changes[10] >0 ):
                        changes[5] -= 1
                        changes[10] -= 1
                    elif changes[5] > 2:
                        changes[5] -= 3
                    else:
                        return False
            else:
                changes[5] += 1
        return True

                        
# @lc code=end

