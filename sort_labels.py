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
import sys

label_fpath = 'labels.tsv'

if not os.path.exists(label_fpath):
    print(label_fpath + ' does not exist!', file=sys.stderr)
    sys.exit(-1)

label_file_lines = open(label_fpath, mode='r', encoding='utf-8').readlines()
label_file_lines.sort()

with open(label_fpath, mode='wb') as outfile:
    for line in label_file_lines:
        outfile.write(line.encode('utf-8'))
