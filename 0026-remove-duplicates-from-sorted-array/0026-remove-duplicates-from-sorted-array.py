class Solution(object):
    def removeDuplicates(self, nums):
        unique = set()
        i=0
        while i<len(nums):
            if nums[i] not in unique:
                unique.add(nums[i])
                i+=1
            else:
                m=i
                while nums[i] in unique:
                    i+=1
                    if i == len(nums):
                        return len(unique)
                unique.add(nums[i])
                nums[i],nums[m]=nums[m],nums[i]
                i = m+1
        return len(unique)