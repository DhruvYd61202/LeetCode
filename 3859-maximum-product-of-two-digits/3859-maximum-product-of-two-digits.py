class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        i=0
        while n!=0:
            i = n%10
            digits.append(i) 
            n=n//10
        digits.sort(reverse=True)
        return digits[0]*digits[1]