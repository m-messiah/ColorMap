#!/usr/bin/python
# -*- coding: utf-8 -*-
import pickle
import sys


def __toLand__(line):
    a = line.split(' ')
    a = [(float(a[i]), float(a[i + 1])) for i in range(len(a) - 1) if i % 2 == 0]
    a.append(a[0])
    a = [(a[i], a[i + 1]) for i in range(len(a) - 1)]
    return a


class Reader(object):
    def __init__(self, filename, method):
        self.filename = filename
        self.lands = []
        if method == 0:
            self.read_map_text()
        else:
            self.read_map_pickle()

    def read_map_text(self):
        try:
            in_file = open(self.filename)
            n = int(in_file.readline())
            for i in range(n):
                self.lands.append(__toLand__(in_file.readline()))
        except IOError:
            print 'Can`t open file ', self.filename
            sys.exit(1)
        except Exception:
            print 'Incorrect file', self.filename, ' You can try to change format of file throw option `-f`'
            sys.exit(2)

    def read_map_pickle(self):
        """Read map from a source file"""
        try:
            in_file = open(self.filename)
            n = int(in_file.readline())
            for i in range(n):
                self.lands.append(pickle.load(in_file))
        except IOError:
            print 'Can`t open file ', self.filename
            sys.exit(1)
        except:
            print 'Incorrect file', self.filename, ' You can try to change format of file throw option `-f`'
            sys.exit(2)
