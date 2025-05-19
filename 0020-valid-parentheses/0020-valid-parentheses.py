class Solution:
    def isValid(self, s):
    # Initialize an empty list to use as a stack
        brackets = []

        # Dictionary to define matching pairs for closing brackets
        pairs = {
            ')': '(',   # closing round bracket matches opening round
            '}': '{',   # closing curly bracket matches opening curly
            ']': '['    # closing square bracket matches opening square
        }

        # Iterate over each character in the input string
        for char in s: 
            # If the character is not a closing bracket, it's an opening bracket
            if char not in pairs:
                # Push the opening bracket onto the stack
                brackets.append(char)
                # Debug print to see the stack at this point (optional)
                # print(brackets)
            # If the character is a closing bracket
            elif not brackets or brackets[-1] != pairs[char]:
                # If the stack is empty OR the top doesn't match the corresponding opening bracket
                return False
            else:
                # Pop the matching opening bracket from the stack
                brackets.pop()

        # After processing all characters, stack should be empty if valid
        return len(brackets) == 0

# Test the function with a valid bracket string
# print(isValid("()[]{}"))  # Output: True
