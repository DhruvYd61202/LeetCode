class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final_pos = len(nums) - 1
        for idx in range(len(nums)-1,-1,-1):
            if idx + nums[idx] >= final_pos:
                final_pos = idx
        return True if final_pos == 0 else False 
        