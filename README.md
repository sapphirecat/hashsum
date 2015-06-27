# hashsum
File hash calculator in Python3, mainly useful for win32.

# what?
I decided that I _really should_ verify downloads and not trust them blindly anymore.
I didn’t have a win32 hash calculator installed, and without one, I couldn’t verify any of them.

Luckily, I had Python already and its standard library has hash functions.

I still haven’t downloaded a ‘real’ hash verifier.

# usage

    [python.exe] hashsum.py FILENAME

I tried using `sys.argv[1:]` but Windows decided to pass `; echo HASH` as three more filenames.
I don’t even.

If you’re on Linux/OS X you may have `sha1sum`/`sha256sum` (or just `shasum`) already.

# license
Since this is barely even a thing: MIT.
