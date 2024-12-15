class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res=""
        if numRows==1 or numRows>len(s):
            return s
        
        for i in range(numRows):
            l=(numRows-1)*2
            for j in range(i,len(s),l):
                res+=s[j]
                if i < numRows-1 and i>0 and j+l-i*2<len(s):
                    res+=s[j+l-i*2]
            
        return res
                    
                
