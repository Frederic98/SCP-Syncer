#!/usr/bin/env python3
import argparse
import os
import pickle
import subprocess
import re

hashers = {'sha1': 'sha1sum',
           'sha256': 'sha256sum',
           'sha512': 'sha512sum',
           'md5': 'md5sum'}

parser = argparse.ArgumentParser(description='Calculate hashes of files recursively')
parser.add_argument('path', default='./', nargs='?', help='The path to search in')
parser.add_argument('output', default='hashes.pkl', nargs='?', help='Output file (pickle)')
parser.add_argument('--hash', choices=hashers.keys(), default='sha1')
args = parser.parse_args()

hasher = hashers[args.hash]
HASH_RE = re.compile(r'(?P<hash>[a-z\d]+) +(?P<file>.*)')
hashes = {}
for root, dirs, files in os.walk(args.path):
    # print(root)
    if files:
        cmd = [hasher]
        cmd.extend([os.path.join(root, file) for file in files])
        hash_str = subprocess.check_output(cmd, universal_newlines=True)
        for match in HASH_RE.finditer(hash_str):
            fn = os.path.relpath(match.group('file'), args.path)
            hashes[fn] = match.group('hash')

with open(args.output, 'wb') as f:
    pickle.dump(hashes, f)
