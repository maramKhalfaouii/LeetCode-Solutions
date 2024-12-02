class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        farthest =0
        r,l,res=0,0,0
        while r < len(nums)-1:
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r+1
            r=farthest
            res+=1
        return res
            
        