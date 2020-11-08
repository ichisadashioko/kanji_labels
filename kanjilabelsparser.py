#!/usr/bin/env python3
# encoding=utf-8
import os


def parse_formatted_labels(content: str, verbose=False):
    lines = content.splitlines(keepends=False)

    if verbose:
        print('number of lines:', len(lines))

    num_lines = len(lines)

    retval = []

    for line_idx in range(num_lines):
        line = lines[line_idx]

        if len(line) == 0:
            pass
            # print(line_idx)
        else:
            cols = line.split('\t')

            if len(cols) == 1:
                category_chars = cols[0]
            elif len(cols) > 1:
                category_chars = cols[0] + cols[1]
            else:
                print(repr(line))
                raise Exception('Cannot parse line ' + repr(line_idx) + '!')

            retval.append(category_chars)

    if verbose:
        print('number of categories:', len(retval))

    return retval


if __name__ == '__main__':
    infile = os.path.join(
        os.path.dirname(__file__),
        'labels.tsv',
    )

    content = open(infile, mode='rb').read()
    content = content.decode('utf-8')

    label_categories = parse_formatted_labels(
        content=content,
        verbose=True,
    )
