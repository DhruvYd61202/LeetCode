class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        idx=0
        while idx < n and citations[idx] > idx:
            idx += 1
        return idx