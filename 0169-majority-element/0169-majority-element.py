class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        major_ele=0
        for i in range(len(nums)):
            if count==0:
                major_ele=nums[i]
            if(major_ele==nums[i]):
                count+=1
            else: count -=1
        return major_ele       