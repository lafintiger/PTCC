#!/usr/bin/env python3
"""
Run script for PenTest Command Center.
This script simply imports and runs the main app.py file.
"""

import os
import sys

# Add the pentest_command_center directory to the path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pentest_command_center'))

# Import and run the app
if __name__ == "__main__":
    from pentest_command_center.app import app
    # Launch the app
    app.launch(share=False) 