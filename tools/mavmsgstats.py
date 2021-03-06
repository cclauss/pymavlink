#!/usr/bin/env python

'''
show stats on messages in a log
'''

import os

from argparse import ArgumentParser
parser = ArgumentParser(description=__doc__)
parser.add_argument("logs", metavar="LOG", nargs="+")

args = parser.parse_args()

from pymavlink import mavutil

def show_stats(logfile):
    '''show stats on a file'''
    print("Processing log %s" % filename)
    mlog = mavutil.mavlink_connection(filename)
    total_size = 0
    names = mlog.name_to_id.keys()
    pairs = []
    for name in names:
        mid = mlog.name_to_id[name]
        count = mlog.counts[mid]
        mlen = mlog.formats[mid].len
        total_size += count * mlen
        pairs.append((name, count*mlen))
    pairs = sorted(pairs, key = lambda p : p[1])
    print("Total size: %u" % total_size)
    for (name,size) in pairs:
        print("%-4s %.2f%%" % (name, 100.0 * size / total_size))

for filename in args.logs:
    show_stats(filename)
