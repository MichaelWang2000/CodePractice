class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(len(s)):
            if t.find(s[i]) < 0:
                return False
            if i != 0 and t.find(s[i - 1]) > t.find(s[i]):
                return False
        return True
s = "abc"
t = "ahbgdc"
a = Solution()
if a.isSubsequence(s,t):
    print('haha')
else:
    print('shit')