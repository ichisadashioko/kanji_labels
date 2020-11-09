#!/usr/bin/env python3
# encoding=utf-8
import os
import sys

uniqueness_log = {}

label_fpath = 'labels.tsv'

if not os.path.exists(label_fpath):
    print(label_fpath + ' does not exist!', file=sys.stderr)
    sys.exit(-1)

label_file_content = open(label_fpath, mode='r', encoding='utf-8').read()

line_num = 0
char_num = 0

for c in label_file_content:

    if c == '\n':
        line_num += 1
        char_num = 0
        continue
    elif c == '\t':
        char_num += 1
        continue
    else:
        if c in uniqueness_log:
            print(repr(c) + ' has already existed at ', file=sys.stderr)
            print(uniqueness_log[c], file=sys.stderr)
            sys.exit(-1)
        else:
            uniqueness_log[c] = {
                'fpath': label_fpath,
                'line_num': line_num,
                'char_num': char_num,
            }

            char_num += 1

missing_chars_fpath = 'missing_chars.txt'

if not os.path.exists(missing_chars_fpath):
    print(missing_chars_fpath + ' does not exist!', file=sys.stderr)
    sys.exit(-1)

missing_chars_content = open(missing_chars_fpath, mode='r', encoding='utf-8').read()

line_num = 0
char_num = 0

for c in missing_chars_content:

    if c == '\n':
        line_num += 1
        char_num = 0
        continue
    elif c == '\t':
        char_num += 1
        continue
    else:
        if c in uniqueness_log:
            print(repr(c) + ' has already existed at ', file=sys.stderr)
            print(uniqueness_log[c], file=sys.stderr)
            sys.exit(-1)
        else:
            uniqueness_log[c] = {
                'fpath': missing_chars_fpath,
                'line_num': line_num,
                'char_num': char_num,
            }

            char_num += 1

sys.exit(0)
