#!/usr/bin/python
# -*- coding: utf-8 -*-
from Geometry import *
##########################################
class Graph(object):
    def __init__(self, lands):
        """Creates graph of subcontracting from a map"""
        self.lands = lands
        graph = [[i, ] for i in range(len(self.lands))]
        for a in graph:
            for b in self.lands:
                if (self.lands[a[0]] != b) and (subcontract(self.lands[a[0]], b)):
                    a.append(b)
        self.graph = graph

    ##########################################
    def sort_graph(self):
        """Sort graph by amount of subcontracting"""
        graph = self.graph
        graph.sort(lambda x, y: cmp(len(x), len(y)))
        graph.reverse()
        self.graph = graph

    ##########################################
    def colorize(self):
        """Colorize map"""
        graph = self.graph
        lands = self.lands
        color = [0] * len(lands)
        j = 0
        k = 0
        first = 0
        while k < len(lands):
            j += 1
            for i in range(len(lands)):
                if color[i] == 0:
                    first = i
                    color[first] = j
                    k += 1
                    break
            for i in range(len(lands)):
                x = 0
                for l in range(len(lands)):
                    if color[l] == j:
                        x += subcontract(lands[graph[l][0]], lands[graph[i][0]])
                if color[i] == 0 and subcontract(lands[graph[i][0]], lands[graph[first][0]]) == 0 and x == 0:
                    color[i] = j
                    k += 1
        self.color = color
