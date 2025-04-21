import traceback

try:
    from pentest_command_center.app import app
    print('Successfully imported app module')
except Exception as e:
    print(f'Error importing app: {e}')
    traceback.print_exc()
    
    # Try to extract the most relevant part of the traceback
    tb = traceback.extract_tb(e.__traceback__)
    print("\nMost recent call last:")
    for frame in tb[-5:]:  # Show the last 5 frames
        print(f"  File \"{frame.filename}\", line {frame.lineno}, in {frame.name}")
        print(f"    {frame.line}") 