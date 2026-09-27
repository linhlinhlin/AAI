"""Load an executable from a framed stream, then replace this process with it.

Remaining stdin belongs to the program. Oracles stay on the host; no host mount,
shared output file or child-authored JSON can determine the verdict.
"""
import os
import struct


def read_exact(size):
    data = bytearray()
    while len(data) < size:
        chunk = os.read(0, size - len(data))
        if not chunk:
            raise SystemExit(125)
        data.extend(chunk)
    return data


size = struct.unpack('!I', read_exact(4))[0]
if not 0 < size <= 4 * 1024 * 1024:
    raise SystemExit(125)
with open('/work/program', 'wb') as stream:
    stream.write(read_exact(size))
os.chmod('/work/program', 0o500)
os.execve('/work/program', ['/work/program'], {'LANG': 'C.UTF-8', 'PATH': '/usr/bin:/bin'})
