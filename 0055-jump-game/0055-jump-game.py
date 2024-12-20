class Solution(object):
    def canJump(self, nums):
        target_num_index = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if target_num_index <= i + nums[i]:
                target_num_index = i
        return target_num_index == 0
               