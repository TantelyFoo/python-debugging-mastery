"""
Python Debugging Environment Setup Script

This script helps you set up your Python debugging learning environment
with all the necessary tools and configurations.
"""

import os
import sys
import subprocess
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible."""
    print("🐍 Checking Python version...")
    version = sys.version_info
    
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible")
        print("   Please install Python 3.8 or higher")
        return False


def create_virtual_environment():
    """Create a virtual environment for the debugging course."""
    print("\n🏗️  Creating virtual environment...")
    
    venv_path = Path("debugging_env")
    
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True
    
    try:
        subprocess.run([sys.executable, "-m", "venv", "debugging_env"], 
                      check=True)
        print("✅ Virtual environment created successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return False


def get_activation_command():
    """Get the command to activate the virtual environment."""
    if os.name == 'nt':  # Windows
        return "debugging_env\\Scripts\\activate"
    else:  # Unix/Linux/macOS
        return "source debugging_env/bin/activate"


def install_packages():
    """Install required packages."""
    print("\n📦 Installing required packages...")
    
    # Determine pip executable path
    if os.name == 'nt':  # Windows
        pip_exe = Path("debugging_env/Scripts/pip.exe")
    else:  # Unix/Linux/macOS
        pip_exe = Path("debugging_env/bin/pip")
    
    if not pip_exe.exists():
        print("❌ Virtual environment pip not found")
        return False
    
    try:
        # Upgrade pip first
        subprocess.run([str(pip_exe), "install", "--upgrade", "pip"], 
                      check=True)
        
        # Install requirements
        subprocess.run([str(pip_exe), "install", "-r", "requirements.txt"], 
                      check=True)
        
        print("✅ All packages installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install packages: {e}")
        return False


def create_vscode_config():
    """Create VS Code configuration for debugging."""
    print("\n⚙️  Creating VS Code configuration...")
    
    vscode_dir = Path(".vscode")
    vscode_dir.mkdir(exist_ok=True)
    
    # Launch configuration for debugging
    launch_config = {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "justMyCode": True
            },
            {
                "name": "Python: Current File (Debug Mode)",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "justMyCode": False,
                "stopOnEntry": True
            },
            {
                "name": "Python: Exercise Debug",
                "type": "python",
                "request": "launch",
                "program": "${workspaceFolder}/exercises/${fileBasenameNoExtension}.py",
                "console": "integratedTerminal",
                "justMyCode": True
            }
        ]
    }
    
    # Settings for Python debugging
    settings_config = {
        "python.defaultInterpreterPath": "./debugging_env/Scripts/python.exe" if os.name == 'nt' else "./debugging_env/bin/python",
        "python.terminal.activateEnvironment": True,
        "python.linting.enabled": True,
        "python.linting.pylintEnabled": True,
        "python.formatting.provider": "black",
        "editor.formatOnSave": True,
        "python.testing.pytestEnabled": True,
        "python.testing.unittestEnabled": False,
        "python.testing.nosetestsEnabled": False
    }
    
    import json
    
    # Write launch.json
    with open(vscode_dir / "launch.json", "w") as f:
        json.dump(launch_config, f, indent=4)
    
    # Write settings.json
    with open(vscode_dir / "settings.json", "w") as f:
        json.dump(settings_config, f, indent=4)
    
    print("✅ VS Code configuration created")
    return True


def create_sample_debug_script():
    """Create a sample script for testing the debugging setup."""
    print("\n📝 Creating sample debug script...")
    
    sample_script = '''"""
Sample debugging script to test your environment setup.

Run this script to verify that your debugging environment is working correctly.
Try setting breakpoints and stepping through the code.
"""

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def fibonacci(n):
    """Calculate fibonacci number (intentionally inefficient for debugging)."""
    logger.debug(f"Calculating fibonacci({n})")
    
    if n <= 0:
        logger.warning("Invalid input: n should be positive")
        return 0
    elif n == 1:
        logger.debug("Base case: n=1, returning 1")
        return 1
    elif n == 2:
        logger.debug("Base case: n=2, returning 1")
        return 1
    else:
        logger.debug(f"Recursive case: calculating fib({n-1}) + fib({n-2})")
        result = fibonacci(n-1) + fibonacci(n-2)
        logger.debug(f"fibonacci({n}) = {result}")
        return result


def test_debugging():
    """Test function for debugging practice."""
    logger.info("Starting debugging test")
    
    # Test basic functionality
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    print("Testing fibonacci calculations:")
    for num in numbers:
        result = fibonacci(num)
        print(f"fibonacci({num}) = {result}")
        
        # Add assertion for testing
        assert result >= 0, f"Fibonacci result should be non-negative, got {result}"
    
    logger.info("Debugging test completed successfully")


if __name__ == "__main__":
    print("🧪 Python Debugging Environment Test")
    print("="*40)
    
    # Test print debugging
    print("Testing print debugging...")
    
    # Test logging
    logger.info("Testing logging functionality")
    
    # Test assertions
    try:
        assert True, "This assertion should pass"
        logger.debug("Assertion test passed")
    except AssertionError as e:
        logger.error(f"Assertion failed: {e}")
    
    # Run the main test
    test_debugging()
    
    print("\\n✅ Environment test completed!")
    print("\\n🎯 Next steps:")
    print("1. Set breakpoints in this file")
    print("2. Run with F5 in VS Code")
    print("3. Practice stepping through code")
    print("4. Inspect variables in the debugger")
'''
    
    with open("test_environment.py", "w") as f:
        f.write(sample_script)
    
    print("✅ Sample debug script created: test_environment.py")
    return True


def display_next_steps():
    """Display next steps for the user."""
    activation_cmd = get_activation_command()
    
    print("\n" + "="*60)
    print("🎉 SETUP COMPLETED SUCCESSFULLY!")
    print("="*60)
    
    print("\n📋 NEXT STEPS:")
    print(f"1. Activate virtual environment:")
    print(f"   {activation_cmd}")
    
    print("\n2. Open VS Code in this directory:")
    print("   code .")
    
    print("\n3. Test your debugging setup:")
    print("   python test_environment.py")
    
    print("\n4. Start with Phase 1:")
    print("   cd 01_basic_debugging")
    print("   python 01_print_debugging.py")
    
    print("\n5. Track your progress:")
    print("   Edit PROGRESS.md to mark completed items")
    
    print("\n🤖 GitHub Copilot Chat Tips:")
    print("• Ask specific debugging questions with context")
    print("• Request code reviews for debuggability")
    print("• Get help with debugging strategies")
    print("• Ask for explanations of debugging concepts")
    
    print("\n📚 Learning Resources:")
    print("• Read README.md for complete course overview")
    print("• Follow the phase-by-phase structure")
    print("• Complete exercises in the exercises/ directory")
    
    print("\n" + "="*60)


def main():
    """Main setup function."""
    print("🚀 Python Debugging Mastery - Environment Setup")
    print("="*50)
    
    # Check prerequisites
    if not check_python_version():
        return False
    
    # Setup steps
    setup_steps = [
        create_virtual_environment,
        install_packages,
        create_vscode_config,
        create_sample_debug_script,
    ]
    
    for step in setup_steps:
        if not step():
            print(f"\n❌ Setup failed at step: {step.__name__}")
            return False
    
    # Show next steps
    display_next_steps()
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
