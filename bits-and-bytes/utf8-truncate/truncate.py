import sys

def truncate(s, n):
    if n >= len(s):
        return s
    while n > 0 and (s[n] & 0xc0) == 0x80:
        n -= 1
    return s[:n]

with open('cases', 'rb') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        sys.stdout.buffer.write(truncate(line[1:-1], line[0]) + b'\n')
