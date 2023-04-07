"""
1. Read from stdin, search/replace hex, write to stdout
2. Convert hex to rgb form to cover simple.css
3. Fix advanced.css: alpha channel, abbrev form
4. Refactor
"""

import re
import sys

HEXCODES = dict(zip('0123456789abcdef', range(16)))

# Input: Two character hexadecimal or byte string
# Output: Decimal integer representation of hex value
def byte_to_dec(byte_str):
    return ((HEXCODES[byte_str[0]] << 4) + # multiply by 16
            (HEXCODES[byte_str[1]]))

# Input: Regex object
# Output: String representation of decimal value
def hex_to_rgb(r):
    hex_str = r.group(1)
    dec_ints = [byte_to_dec(hex_str[i: i + 2]) for i in (0, 2, 4)]
    return 'rgb(%s)' % (','.join(str(d) for d in dec_ints))

output = re.sub(r'\#([0-9a-fA-F]+)', hex_to_rgb, sys.stdin.read())
sys.stdout.write(output)

print("ok")
