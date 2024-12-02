class Solution(object):
    def majorityElement(self, nums):
        hash=dict()
        for i in nums:
            if i in hash.keys():
                hash[i]+=1
            else:
                hash[i]=1
        
        f=0
        maj=-1
        for i in hash:
            if hash[i]>f:
                f=hash[i]
                res=i
        return res
        