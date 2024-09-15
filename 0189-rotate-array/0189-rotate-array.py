class Solution(object):
    def reverse(self, array, start, end):
        while start < end:
            array[start], array[end]=array[end], array[start]
            start+=1
            end-=1
            
    def rotate(self, nums, k):
        k%=len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        
        

            
            
        