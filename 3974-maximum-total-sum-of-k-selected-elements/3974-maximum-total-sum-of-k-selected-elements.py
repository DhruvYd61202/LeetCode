class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort()

        # Base sum of largest k elements
        ans = sum(nums[-k:])

        t = min(k, mul - 1)

        # Extra gain from multiplication
        for j in range(t):
            ans += nums[-1 - j] * (mul - 1 - j)

        return ans
        