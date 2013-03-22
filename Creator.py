#!/usr/bin/python
# -*- coding: utf-8 -*-
import pickle


##########################################
class Creator(object):
    def __init__(self, filename, method):
        self.filename = filename
        if method == 0:
            self.create_map_text()
        else:
            self.create_map_pickle()

    def create_map_text(self):
        o_file = open(self.filename, "w")
        o_file.write("4\n")
        a = (((0.5, 0.5), (1, 1)), ((1, 1), (1, 0)), ((1, 0), (0.5, 0)), ((0.5, 0), (0.5, 0.5)))
        for i in range(len(a)):
            o_file.write("{0} {1} ".format(a[i][0][0], a[i][0][1]))
        o_file.write("\n")
        a = (((0, 0), (0.5, 0.5)), ((0.5, 0.5), (0.5, 0)), ((0.5, 0), (0, 0)))
        for i in range(len(a)):
            o_file.write("{0} {1} ".format(a[i][0][0], a[i][0][1]))
        o_file.write("\n")
        a = (((1, 0), (1, 1)), ((1, 1), (2, 1)), ((2, 1), (2, 0)), ((2, 0), (1, 0)))
        for i in range(len(a)):
            o_file.write("{0} {1} ".format(a[i][0][0], a[i][0][1]))
        o_file.write("\n")
        a = (((0, 1), (0, 2)), ((0, 2), (2, 2)), ((2, 2), (2, 1)), ((2, 1), (0, 1)))
        for i in range(len(a)):
            o_file.write("{0} {1} ".format(a[i][0][0], a[i][0][1]))
        o_file.close()

    def create_map_pickle(self):
        """Creates map"""
        o_file = open(self.filename, "w")
        o_file.write("4\n")
        a = (((0.5, 0.5), (1, 1)), ((1, 1), (1, 0)), ((1, 0), (0.5, 0)), ((0.5, 0), (0.5, 0.5)))
        pickle.dump(a, o_file)
        a = (((0, 0), (0.5, 0.5)), ((0.5, 0.5), (0.5, 0)), ((0.5, 0), (0, 0)))
        pickle.dump(a, o_file)
        a = (((1, 0), (1, 1)), ((1, 1), (2, 1)), ((2, 1), (2, 0)), ((2, 0), (1, 0)))
        pickle.dump(a, o_file)
        a = (((0, 1), (0, 2)), ((0, 2), (2, 2)), ((2, 2), (2, 1)), ((2, 1), (0, 1)))
        pickle.dump(a, o_file)
        o_file.close()


def map2text(land, filename):
    try:
        o_file = open(filename, 'w')
        o_file.write("{0}\n".format(len(land)))
        for a in land:
            for i in range(len(a)):
                o_file.write("{0} {1} ".format(a[i][0][0], a[i][0][1]))
            o_file.write("\n")
        o_file.close()
    except:
        print 'Can`t work with file ', filename
