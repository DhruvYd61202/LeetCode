import os

root_dir = 'LeetCode'  # Change if needed
valid_extensions = ('.py', '.sql')

count = 0
for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        if file.endswith(valid_extensions):
            count += 1

print(f"Counted {count} solution files")

readme_path = 'README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

found_marker = False
with open(readme_path, 'w', encoding='utf-8') as f:
    for line in lines:
        if "Solved LeetCode Problems" in line:
            new_line = f"### ✅ Solved LeetCode Problems: **`{count}`**\n"
            f.write(new_line)
            found_marker = True
            print(f"Updated line to: {new_line.strip()}")
        else:
            f.write(line)

if not found_marker:
    print("Marker line not found in README.md")
