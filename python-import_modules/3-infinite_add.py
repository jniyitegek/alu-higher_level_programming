#!/usr/bin/python3
import sys

# Sum all arguments starting from index 1 (skipping script name)
total = sum(int(arg) for arg in sys.argv[1:])

# Print the total sum
print(total)
