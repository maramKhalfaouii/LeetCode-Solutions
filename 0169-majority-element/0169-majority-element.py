class Solution(object):
    def majorityElement(self, nums):
        hash={}
        f=0
        maj=-1
        for i in nums:
            hash[i] = 1 + hash.get(i, 0)
            if hash[i]>maj:
                res=i
                maj=hash[i]
        return res
        