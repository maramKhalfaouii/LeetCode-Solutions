class Solution(object):
    def removeDuplicates(self, nums):
        k,n=0,len(nums)
        for i in range(n):
            if i+2>=len(nums) or nums[i]!=nums[i+2]:
                nums[k]=nums[i]
                k+=1
        return k
        