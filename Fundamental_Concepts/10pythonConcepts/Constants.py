from typing import Final

# Declare constants with Final
VERSION: Final[str] = "1.0.0"
PI: Final[float] = 3.14159

# Attempt to reassign the constants
VERSION = "1.0.1"  # This should raise a mypy warning
PI = 3.14  # This should also raise a mypy warning

print(VERSION)
print(PI)
