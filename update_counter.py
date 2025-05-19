import os

root_dir = 'LeetCode'  # Your root folder with all problem folders
valid_extensions = ('.py', '.cpp', '.java')  # Adjust if needed

count = 0
for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        if file.endswith(valid_extensions):
            count += 1

readme_path = 'README.md'
with open(readme_path, 'r') as f:
    lines = f.readlines()

with open(readme_path, 'w') as f:
    for line in lines:
        if line.startswith("### ✅ Solved LeetCode Problems"):
            f.write(f"### ✅ Solved LeetCode Problems: **'{count}'**\n")
        else:
            f.write(line)
