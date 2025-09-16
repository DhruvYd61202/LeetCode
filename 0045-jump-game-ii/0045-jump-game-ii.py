class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        total_jumps = 0
        destination = len(nums) - 1
        coverage =0
        lastjumpIdx = 0
        
        # base case
        if len(nums) == 1:
            return 0

        # Greedy strategy : extend coverage as long as possible
        for i in range(0,len(nums)):
            coverage = max(coverage, i + nums[i])

            if i == lastjumpIdx:
                lastjumpIdx = coverage
                total_jumps += 1

                if coverage >= destination:
                    return total_jumps
        return total_jumps
        