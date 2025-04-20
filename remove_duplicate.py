#!/usr/bin/env python3

with open('pentest_command_center/app.py', 'r') as f:
    lines = f.readlines()

in_duplicate = False
new_lines = []

for i, line in enumerate(lines):
    if '# LLM Pen Testing Tab' in line and i < 4000:  # Only match the first occurrence
        in_duplicate = True
    elif '# System Backdoors Tab' in line:
        if in_duplicate:
            in_duplicate = False
        new_lines.append(line)
    elif not in_duplicate:
        new_lines.append(line)

with open('pentest_command_center/app.py', 'w') as f:
    f.writelines(new_lines)

print("Removed duplicate LLM Pen Testing tab") 