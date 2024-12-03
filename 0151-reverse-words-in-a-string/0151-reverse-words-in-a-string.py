class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        # res=words[-1]
        # for i in range(len(words)-2,-1,-1):
        #     res+=" "+words[i]
        # return res
        words=list(words)
        reversedWord= words[::-1]
        return " ".join(reversedWord)

        