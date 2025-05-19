import os

# Folder name where your solutions are stored
directory = 'LeetCode_Solutions'
extensions = ('.py', '.cpp', '.java')  # Add/remove as needed

# Count files with the correct extensions
count = sum(1 for file in os.listdir(directory) if file.endswith(extensions))

# Read README.md and update the counter line
with open("README.md", "r") as f:
    lines = f.readlines()

with open("README.md", "w") as f:
    for line in lines:
        if line.startswith("### ✅ Solved LeetCode Problems"):
            f.write(f"### ✅ Solved LeetCode Problems: **`{count}`**\n")
        else:
            f.write(line)
