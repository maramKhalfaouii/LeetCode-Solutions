class Solution(object):
    def titleToNumber(self, columnTitle):
        # res = 0
        # for ch in columnTitle:
        #     res = res * 26 + ord(ch)-ord('A')+1
        # return res     
        return functools.reduce(lambda total, ch:total*26+ord(ch)-ord('A')+1,columnTitle, 0)