#!/usr/bin/env python3
import sys
import os
import site


def main() -> None:
    # sys.prefix != sys.base_prefix means we ARE inside a virtual environment
    # os.environ.get('VIRTUAL_ENV') is another way to check the same thing
    if sys.prefix == sys.base_prefix and not os.environ.get('VIRTUAL_ENV'):
        print("MATRIX STATUS: You're still plugged in\n")
        # Route to python interpreter
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: "
              f"{os.environ.get('VIRTUAL_ENV')} detected")
        print("WARNING: You're in the global environment!\n"
              "The machines can see everything you install.")
        print("To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\\activate  # On Windows\n"
              "Then run this program again.")
        return
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: "
          f"{os.path.basename(os.environ.get('VIRTUAL_ENV'))}")
    print(f"Environment Path: {os.environ.get('VIRTUAL_ENV')}")
    print("SUCCESS: You're in an isolated environment!\n"
          "Safe to install packages without affecting\n"
          "the global system.\n")
    print(f"Package installation path:\n{site.getsitepackages()[0]}")


if __name__ == "__main__":
    main()
