class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #initializing the sum window
        sum_window = sum(nums[:k])
        #initilaizing the max_sum
        max_sum = sum_window

        for i in range(k, len(nums)):
            sum_window += nums[i] - nums[i - k]
            max_sum = max(max_sum, sum_window)

        return max_sum / k