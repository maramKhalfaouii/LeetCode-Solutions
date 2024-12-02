class Solution(object):
    def removeElement(self, nums, val):
        ans=0
        n,k=len(nums)-1,0
        while n>=0 and k<=n:
            if nums[n]==val:
                nums[n]='-'
                n-=1
            else:
                ans+=1
                nums[n],nums[k]=nums[k], nums[n]
                k+=1

        return ans
        