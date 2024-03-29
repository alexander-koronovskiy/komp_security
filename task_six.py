import zlib
from array import array

poly = 0xEDB88320

table = array('L')
for byte in range(256):
    crc = 0
    for bit in range(8):
        if (byte ^ crc) & 1:
            crc = (crc >> 1) ^ poly
        else:
            crc >>= 1
        byte >>= 1
    table.append(crc)


def crc32(string):
    value = 0xffffffff
    for ch in string:
        value = table[(ord(ch) ^ value) & 0xff] ^ (value >> 8)

    return -1 - value


my_file = open("text_6.txt")
text = my_file.read()
# text = 'A long string to test CRC32 functions'

test_b = bytes(text, 'ansi')
b = crc32(text)

print('hand-made hash sum: ', '%08x' % (b & 0xffffffff))
print('python z-lib hash sum: ', hex(zlib.crc32(test_b))[2:])
