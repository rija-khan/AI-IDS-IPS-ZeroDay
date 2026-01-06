"""
Network Test Script
Run this first to check your system
"""

import sys
import platform

def check_system():
    print("🖥️  SYSTEM DIAGNOSTIC TOOL")
    print("="*50)
    
    # Check Python
    print(f"\n✅ Python Version: {sys.version}")
    
    # Check OS
    print(f"✅ Operating System: {platform.system()} {platform.release()}")
    
    # Check if we can import required packages
    packages = ["scapy", "sklearn", "pandas", "numpy", "matplotlib"]
    
    print("\n📦 CHECKING REQUIRED PACKAGES:")
    for package in packages:
        try:
            __import__(package)
            print(f"   ✓ {package}")
        except ImportError:
            print(f"   ✗ {package} (install with: pip install {package})")
    
    print("\n" + "="*50)
    print("🎯 NEXT STEPS:")
    print("1. If all packages show ✓, run: python demo.py")
    print("2. If any show ✗, run: pip install -r requirements.txt")
    print("3. Contact your teacher if you need help")
    print("="*50)

if __name__ == "__main__":
    check_system()
    input("\nPress Enter to exit...")
