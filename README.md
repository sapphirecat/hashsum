# hashsum
File hash calculator in Python3, mainly useful for win32.

Runs in Python 3.4 and up.

# what?
I decided that I _really should_ verify downloads and not trust them blindly anymore.
I didn’t have a win32 hash calculator installed, and without one, I couldn’t verify any of them.

Luckily, I had Python already and its standard library has hash functions.

I still haven’t downloaded a ‘real’ hash verifier.

# usage
Abstract:

    [python.exe] hashsum.py [-a ALGO] FILENAME

Examples for Windows:

    py -3 hashsum.py hashsum.py
    py -3 hashsum.py -a sha256 README.md
    py -3 hashsum.py -a md5 LICENSE

Examples for Linux/OS X:

    python3 hashsum.py hashsum.py
    python3 hashsum.py -a sha256 README.md
    python3 hashsum.py -a md5 LICENSE

The `-a` option indicates the hash algorithm to use, such as “sha1”, “sha256”, or “sha384”.
Technically, it takes any of the `hashlib` hash constructors.
“md5” is possible, but considered weak.

If you’re on Linux/OS X you may have `sha1sum`/`sha256sum` (or just `shasum`) already.
Some examples for those commands:

    sha1sum hashsum.py
    sha256sum README.md
    shasum -a 256 LICENSE

# license
Since this is barely even a thing: MIT.
