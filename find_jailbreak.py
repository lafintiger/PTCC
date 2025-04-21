with open('pentest_command_center/app.py', 'r') as f:
    lines = f.readlines()
    
# Search for jailbreak_type
for i, line in enumerate(lines):
    if 'jailbreak_type' in line:
        start = max(0, i-2)
        end = min(len(lines), i+3)
        print(f"\nFound at line {i+1}:")
        for j in range(start, end):
            print(f"Line {j+1}: {lines[j].strip()}")
        print("-" * 80)

print("\n\nLooking at line 3125 and surrounding lines:")
for i in range(3120, 3130):
    print(f"Line {i+1}: {lines[i].strip()}") 