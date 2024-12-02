class Solution(object):
    def removeDuplicates(self, nums):
        k,r,n,ans=1,1,len(nums),1
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                r+=1
                if r < 3:
                    nums[k]=nums[i]
                    ans+=1
                    k+=1
            else:
                r=1
                nums[k]=nums[i+1]
                ans+=1
                k+=1
        return ans
        