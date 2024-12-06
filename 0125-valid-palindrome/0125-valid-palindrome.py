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
        i,j=0,len(newString)-1
        while i<j:
            if newString[i]==newString[j]:
                i+=1
                j-=1
            else: 
                return False
        return True
        