class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x//10==0:
            return True
        s=str(x)
        return s==s[::-1]