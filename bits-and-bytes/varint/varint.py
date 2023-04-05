import struct

# Encode the data into the variable length format
def encode(n):
    '''
    while n > 0:
        take lowest order 7 bits
        add the correct msb (continuation bit)
        push to some sequence of bytes
        reduce n by 7 bits
    return byte sequence
    '''
    out = []
    while n > 0:
        part = n % 128 # TODO: add bitmask for optimization
        n >>= 7
        # add msb
        if n > 0:
            part ^= 0b10000000 # could change to 0x80 to make more readable
        out.append(part)
    return bytes(out)

# Reading in the data
# 'rb' - read in the input file and interpret as binary
with open('150.uint64', 'rb') as f:
    # Convert the bytes to integer representation
    # '>Q' - big endian 64-bit integer code for unpack
    # see help(unpack) for more info
    n = struct.unpack('>Q', f.read())[0] # unpack always returns a sequence
    print(encode(n))
