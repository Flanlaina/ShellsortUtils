#!/usr/bin/env python3

# A Shellsort worst-case input generator, based on Frobenius theory
# and aphitorite's code to generate Shellsort's adversary input.
# Copyright (C) 2026 Quang Lam (Flanlaina)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys

def main(argv):
    if len(sys.argv) != 4:
        print('Usage:')
        print(f'{sys.argv[0]} <length> <infile> <outfile>')
        print('where:')
        print('<length>: length of the output list, in decimal.')
        print('<infile>: name of input file, containing the gap sequence in the form')
        print('          of positive integers, sorted descending, separated by whitespace characters.')
        print('<outfile>: name of output file, containing the resulting list in the form')
        print('          of positive integers separated by spaces.')

        exit(1)

    try:
        length = int(sys.argv[1])
    except ValueError:
        print(f'Error: "{sys.argv[1]}" is not a valid integer!', file=sys.stderr)
        exit(1)

    if length < 1:
        print(f'Error: "{length}" is not a positive integer!', file=sys.stderr)
        exit(1)

    try:
        with open(sys.argv[2], 'r') as fi:
            gaps = list(map(int, fi.read().split()))
    except Exception as e:
        print(f'Error reading input file: {type(e).__name__}: {e}')
        exit(1)

    # count buckets

    k = len(gaps)
    j = k
    arr = [0] * length
    arr[0] = k + 1

    for g in gaps:
        for i in range(g, length):
            if arr[i - g] > 0 and arr[i] == 0:
                arr[i] = j
        j -= 1

    pos = [0] * (k + 2)
    for i in range(length):
        pos[arr[i]] += 1

    for i in range(1, len(pos)):
        pos[i] += pos[i - 1]

    for i in range(length): # iterate forwards instead backwards
        pos[arr[i]] -= 1
        arr[i] = pos[arr[i]] # to reverse order of elements

    try:
        with open(sys.argv[3], 'w') as fo:
            fo.write(' '.join(map(str, arr)))
    except Exception as e:
        print(f'Error writing output file: {type(e).__name__}: {e}')
        exit(1)

if __name__ == '__main__':
    main(sys.argv)
