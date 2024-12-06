class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==1:
            return True
        s = s.lower()
        # for c in s:
        #     if (ord(c)<ord('a') or ord(c)>ord('z')) and not c.isnumeric() :
        #         s = s.replace(c,'')
        a = ''.join(char for char in s if char.isalnum())
        return a==a[::-1]
        