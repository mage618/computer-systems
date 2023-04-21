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
    hex_str = r.group(1).lower()
    # normalize to non-abbreviated form
    if len(hex_str) in {3, 4}:
        hex_str = ''.join(x + x for x in hex_str)
    # computed decimal form of (R, G, B)
    dec_ints = [byte_to_dec(hex_str[i: i + 2]) for i in (0, 2, 4)]
    # maybe compute alpha channel
    if len(hex_str) == 6:
        label = "rgb"
    elif len(hex_str) == 8:
        label = "rgba"
        dec_ints.append('/')
        dec_ints.append("{:.5f}".format(byte_to_dec(hex_str[6:]) / 255))
    else:
        return f'#{hex_str}' # not the best way to validate

    return f'{label}({" ".join(str(d) for d in dec_ints)})'

output = re.sub(r'\#([0-9a-fA-F]+)', hex_to_rgb, sys.stdin.read())
sys.stdout.write(output)

print("ok")
