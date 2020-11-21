#!/usr/bin/env python3
# encoding=utf-8

# Even though I thought that sorting the label categories manually
# would give a boost in performance because those categories look
# similar. However, I realized that Dense layer does not hold the
# relationship between its output nodes. Each output nodes has their
# own weights and they don't really affect the other nodes' weights.

# With that said, we can sort the label categories by their Unicode
# code point of the first character in the category for consistency
# when adding new labels.
import os
import io
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    'infile',
    default='labels.tsv',
    action='store',
    nargs='?',
)

parser.add_argument(
    '--run',
    action='store_true',
)

args = parser.parse_args()
print(args)

label_fpath = args.infile

if not os.path.exists(label_fpath):
    print(label_fpath + ' does not exist!', file=sys.stderr)
    sys.exit(-1)

original_file_bs = open(label_fpath, mode='rb').read()

label_file_lines = original_file_bs.decode('utf-8').splitlines()
label_file_lines.sort()

buffer = io.BytesIO()

for line in label_file_lines:
    buffer.write((line + '\n').encode('utf-8'))

formatted_bs = buffer.getvalue()

if formatted_bs == original_file_bs:
    print('OK')
else:
    print('Need updated!')

    if args.run:
        with open(label_fpath, mode='wb') as outfile:
            outfile.write(formatted_bs)
