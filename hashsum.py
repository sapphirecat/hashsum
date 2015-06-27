# vim:fileencoding=utf-8
# Python 3.4+

import hashlib
import sys
from traceback import print_exc

HASHES = 'sha1 sha256'.split()

def hashfile (name, algo):
    h = hashlib.new(algo)
    try:
        with open(name, 'rb') as f:
            h.update(f.read())
        return h.hexdigest()
    except:
        print_exc()
        print("--" * h.digest_size)

def showfile (f):
    for algo in HASHES:
        print("{1} {2} [{0}]".format(algo, hashfile(f, algo), f))

showfile(sys.argv[1])
