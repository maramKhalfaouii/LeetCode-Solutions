class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l,total,ans=0,0,float("inf")    
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                ans=min(ans,r-l+1)
                total-=nums[l]
                l+=1
        return 0 if ans == float("inf") else ans 