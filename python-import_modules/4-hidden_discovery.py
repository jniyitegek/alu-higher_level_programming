#!/usr/bin/python3
import hidden_4
# Get all names from the module
names = dir(hidden_4)
# Filter and sort names that don't start with '__'
filtered_names = sorted(name for name in names if not name.startswith('__'))
# Print each name
for name in filtered_names:
    print(name)
