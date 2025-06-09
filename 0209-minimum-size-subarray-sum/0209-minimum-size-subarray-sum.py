class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = 0
        minlength = 10000000
        left = 0 #sums= 0
        for right in range(len(nums)):
            sums += nums[right]

            while sums >= target:
                minlength = min(minlength, right - left + 1)
                sums -= nums[left]
                left += 1
        if minlength == 10000000:
            return 0
        return minlength
