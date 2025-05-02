class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if numRows == 1:
        #     return s
        # count = 0
        # result = [[] for _ in range(numRows)]
        # flag = True
        # for i in range(len(s)):
        #     if count < numRows:
        #         result[count].append(s[i])
        #         if flag:
        #             count += 1
        #         else:
        #             count -= 1
        #     if count == numRows:
        #         count -= 2
        #         flag = False
        #     if count == 0:
        #         flag = True
        # return ''.join([i for j in result for i in j])
# print(convert("ADITYASINGH", 3))
        if numRows == 1:
            return s
        res = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for  i in range(r, len(s), increment):
                res += s[i]
                if (r > 0 and r < numRows - 1 and i + increment - 2*r < len(s)):
                    res += s[i + increment - 2*r]
        return res