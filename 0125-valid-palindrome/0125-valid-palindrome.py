class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_str = ''.join([char.lower() for char in s if char.isalnum()])
        return temp_str == temp_str[::-1]
        
       
        
        