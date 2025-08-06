#!/usr/bin/env python3
"""
Simple test runner for the backend
"""
import subprocess
import sys
import os

def install_test_deps():
    """Install test dependencies"""
    print("📦 Installing test dependencies...")
    try:
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Test dependencies installed!")
            return True
        else:
            print("❌ Failed to install test dependencies:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"Error installing dependencies: {e}")
        return False

def run_tests():
    """Run all tests"""
    print("🧪 Running backend tests...")
    print("="*50)
    
    # Change to the backend directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Install test dependencies first
    if not install_test_deps():
        return False
    
    try:
        # Run pytest
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "test_main.py", 
            "-v",  # verbose output
            "--tb=short"  # shorter traceback
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("Errors:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("\n🎉 All tests passed!")
            return True
        else:
            print("\n❌ Some tests failed!")
            return False
            
    except Exception as e:
        print(f"Error running tests: {e}")
        return False

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)