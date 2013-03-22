#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import unittest
from Creator import *
from Reader import *
from Graphs import Graph
from Visual import *
import GeoTests
###################################
parser = argparse.ArgumentParser(description='Map colorizer',
                                 epilog='Input: description of lands on map by set of segments \
    (land is polygon).\n \
    Output: minimal set of colors, needed to colorize this map\n \
    (2 subcontract lands can`t have same colors),and true picture.\n \
    Note: Program with visualization.\n \
    Look for documentation README.md\n')
parser.add_argument('-o', '--open',
                    dest='filename',
                    action='store',
                    help='Opens file `filename`')
parser.add_argument('-f', dest='method', action='store', default=0, type=int,
                    help='Sets input file format. 0-text/1-pickle')
parser.add_argument('-v', '--version',
                    action='version',
                    version='%(prog)s v2.0',
                    help='Show version of the script')


def test():
    unittest.TextTestRunner(verbosity=2).run(GeoTests.start)
parser.add_argument('-t', '--test',
                    '-d', '--debug', dest='test',
                    action='store_const', const=test,
                    help='Run tests')
args = parser.parse_args()
if args.test is not None:
    args.test()
else:   
    #0-text,1-pickle
    method = 0
    if args.method is not None:
        method = args.method
    if args.filename is None:
        filename = "input.txt"
        Creator(filename, method)
    else:
        filename = args.filename
    reader = Reader(filename, method)
    world = Graph(reader.lands)
    world.sort_graph()
    world.colorize()
    visualization(world)
