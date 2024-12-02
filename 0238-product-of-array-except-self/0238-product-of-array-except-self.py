class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        pref = [1] * n
        post = [1] * n
        pref[0]=nums[0]
        for i in range (1,n):
            pref[i]=pref[i-1]*nums[i]
        post[n-1]=nums[n-1]
        for i in range (n-2,-1,-1):
            post[i]=post[i+1]*nums[i]
        for i in range(n):
            if i==0: 
                nums[i]=post[i+1]
            elif i==n-1:
                nums[i]=pref[i-1]
            else:
                nums[i]=pref[i-1]*post[i+1]
        return nums
        

        