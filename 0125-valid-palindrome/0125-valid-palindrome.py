class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newString=""
        if len(s)==1:
            return True
        for c in s:
            if ord(lower(c))>=ord('a') and ord(lower(c))<=ord('z') and c!=" " or c.isnumeric()  :
                newString+=lower(c)
        return newString==newString[::-1]
        