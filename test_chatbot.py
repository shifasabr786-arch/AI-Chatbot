#!/usr/bin/env python3
"""
Simple test script to verify the chatbot setup
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and return success status"""
    print(f"\n{'='*50}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("SUCCESS")
        if result.stdout:
            print("Output:", result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("FAILED")
        print("Error:", e.stderr)
        return False

def main():
    """Main test function"""
    print("Testing Rasa Chatbot Setup")
    print("="*50)
    
    # Check if we're in the right directory
    if not os.path.exists("domain.yml"):
        print("Error: domain.yml not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Test 1: Check Rasa installation
    if not run_command("python -m rasa --version", "Checking Rasa installation"):
        print("Rasa is not installed. Please run: pip install -r requirements.txt")
        sys.exit(1)
    
    # Test 2: Validate configuration
    if not run_command("python -m rasa data validate", "Validating configuration and data"):
        print("Configuration validation failed. Please check your files.")
        sys.exit(1)
    
    # Test 3: Train the model
    if not run_command("python -m rasa train", "Training the chatbot model"):
        print("Model training failed.")
        sys.exit(1)
    
    print("\nAll tests passed! Your chatbot is ready to use.")
    print("\nTo start the chatbot:")
    print("1. Run action server: python -m rasa run actions --actions actions.actions")
    print("2. In another terminal, run: python -m rasa shell")
    print("\nTo test specific scenarios:")
    print("- Ecommerce: 'I need help with my order'")
    print("- Banking: 'I need banking help'")

if __name__ == "__main__":
    main()
