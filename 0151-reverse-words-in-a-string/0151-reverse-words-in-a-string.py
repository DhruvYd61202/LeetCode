class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        s = s.split()
        # print(s)
        # print(type(s))
        s = s[::-1]
        # print(s)
        s = ' '.join(s)
        # print(s)
        return s

        