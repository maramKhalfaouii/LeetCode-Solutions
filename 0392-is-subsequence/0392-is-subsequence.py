class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # i,j=0,0
        # while i<len(s) and j<len(t):
        #     if s[i]==t[j]:
        #         i+=1
        #         j+=1
        #     else:
        #         j+=1
        # return i==len(s)
        i=0
        for c in s:
            if c in t[i:]:
                i=t.index(c,i)+1
            else :
                return False
        return True
        