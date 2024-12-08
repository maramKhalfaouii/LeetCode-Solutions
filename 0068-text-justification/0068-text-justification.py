class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result=[]
        i=0
        temp=[]
        width=0
        while i<len(words):
            if width + len(temp)+len(words[i])>maxWidth:
                extra_space=maxWidth-width
                spaces=extra_space//max(1,len(temp)-1)
                remainder=extra_space%max(1,len(temp)-1)
                for j in range(max(1,len(temp)-1)):
                    temp[j]+=" "*spaces
                    if remainder:
                        temp[j]+=" "
                        remainder-=1
                result.append("".join(temp))
                temp=[]
                width=0
            temp.append(words[i])
            width+=len(words[i])
            i+=1
        last_line=" ".join(temp)
        last_line+=" "*(maxWidth-len(last_line))
        result.append(last_line)
            
        return result
            


