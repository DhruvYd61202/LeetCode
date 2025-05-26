class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        cut=False
        truck1 = 0
        truck2 = 0
        truck3 = 0
        cost=0
        if n<=k and m<=k:
            cost=0
        elif n > k and m<=k:
            cost = (n-k)*(k)
        else:
            cost = (m-k)*k
        return cost
        