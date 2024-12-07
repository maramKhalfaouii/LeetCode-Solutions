class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1]!=9:
            digits[-1]+=1
        else:
            digits[-1]=0
            if len(digits)==1:
                digits.insert(0, 1)
            else: 
                for i in range(len(digits)-2,-1,-1):
                    if i==0 and digits[i]==9:
                        digits[0]=0
                        digits.insert(0, 1)
                        break
                    if digits[i]!=9:
                        digits[i]+=1
                        break
                    else:
                        digits[i]=0
        return digits
        