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


def decode(var_n):
    '''
    for b in var_n (right to left):
        shift accumulator left by 7
        discard msb
        accumulate b
    '''
    n = 0
    for b in reversed(var_n):
        n <<= 7
        b &= 0b01111111 # 0x7f
        n += b
    return n


if __name__ == '__main__':
    cases = (
        ('1.uint64', b'\x01'),
        ('150.uint64', b'\x96\x01'),
        ('maxint.uint64', b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01'),
    )

    for fname, expectation in cases:
        # Reading in the data
        # 'rb' - read in the input file and interpret as binary
        with open(fname, 'rb') as f:
            # Convert the bytes to integer representation
            # '>Q' - big endian 64-bit integer code for unpack
            # see help(unpack) for more info
            n = struct.unpack('>Q', f.read())[0] # unpack always returns a sequence
            # testing encoder
            assert encode(n) == expectation
            assert decode(encode(n)) == n
    print('ok')
