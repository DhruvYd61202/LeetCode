class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplifies a given Unix-style absolute file path.

    Args:
        path (str): A string representing the absolute path.

    Returns:
        str: The simplified canonical path.
    """
        # Stack to store valid directory names
        stack = []
        
        # Split the path by "/" and process each component
        for dir in path.split("/"):
            # Ignore empty strings and "." (current directory)
            if dir == "" or dir == ".":
                continue
            # ".." means go up one directory (pop from stack if not empty)
            elif dir == "..":
                if stack:
                    stack.pop()
            # Valid directory name, add to the stack
            else:
                stack.append(dir)
        
        # Join the stack into a simplified path with leading "/"
        return "/" + "/".join(stack)
    