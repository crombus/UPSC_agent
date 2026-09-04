#!/usr/bin/env python3
"""Customize geo29 generator from geo26 template."""
from pathlib import Path

# Read template
with open('_gen_geo29.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace topic metadata
replacements = [
    ('geography-26', 'geography-29'),
    ('World Population and Demographic Transition', 'Regional Development and Five Year Plans'),
    ('demographic evidence into a qualified spatial argument', 'spatial development evidence into a qualified planning argument'),
]

for old, new in replacements:
    content = content.replace(old, new)

# Write back
with open('_gen_geo29.py', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print('Metadata updated successfully')
