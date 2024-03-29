#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

#if length of query ==1 do help
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
args.seq = args.seq.upper()                 # Note we just added this line

#if contain T is DNA or U RNA
if re.search('^[ACGTU]+$', args.seq):
    if 'T' in args.seq and 'U' in args.seq:
        print('The sequence contains T  and U')
    elif 'T' in args.seq:
        print('The sequence is DNA')
    elif 'U' in args.seq:
        print('The sequence is RNA')
    else:
        print('The sequence is neither standard DNA nor RNA')
else:
    print('The sequence contains invalid characters')

# Print motif
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("IT is!!!")
    else:
        print("NO!")
