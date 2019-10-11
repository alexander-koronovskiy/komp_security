from Hash import *

def get_file_checksum(filename):
    h = SHA384.new()
    chunk_size = 8192
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()