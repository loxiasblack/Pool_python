#!/usr/bin/env python3

import os
import sys


def check_environement() -> bool:
    """check using sys wheter inside virtual env"""
    # prefix == base_prefix we are on global environment
    return sys.prefix != sys.base_prefix


def main() -> None:
    """ check if virtual environment exist"""
    virtual_environment = check_environement()
    if not virtual_environment:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.environ.get('VIRTUAL_ENV')} detected")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install\n")
        print("To enter the construct, run:")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        path = os.getenv("VIRTUAL_ENV")
        print(f"Virtual Environment: {os.path.basename(path)}")
        print(f"Environment Path: {path}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path")
        for path in sys.path:
            if "site-packages" in path:
                print(path)


if __name__ == "__main__":
    main()
