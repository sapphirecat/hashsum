# vim:fileencoding=utf-8
# Python 3.4+

import argparse
import hashlib
import sys
from traceback import print_exc

def hash_file (name, algo):
    h = hashlib.new(algo)
    with open(name, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

def create_arg_parser (**kwargs):
    p = argparse.ArgumentParser(**kwargs)
    p.add_argument('-a', '--algo',
                   default='sha256',
                   help='uses a specific hash algorithm')
    p.add_argument('filename',
                   help='the filename to be hashed')
    return p

def main (argv=None):
    if argv is None:
        argv = sys.argv
    kwargs = dict(prog=argv[0],
                  description='Displays file hashes')
    parser = create_arg_parser(**kwargs)
    opts = parser.parse_args(argv[1:])

    # TODO: study the linux sha1sum output and format this likewise
    hash_out = hash_file(opts.filename, opts.algo)
    print("{0} = {1} {2}".format(hash_out, opts.algo, opts.filename))


if __name__ == '__main__':
    main()
