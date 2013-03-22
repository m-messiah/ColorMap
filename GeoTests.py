#!/usr/bin/python
# -*- coding: utf-8 -*-
from Geometry import *
from random import randint
import unittest


class Test(unittest.TestCase):
    def test_len_one(self):
        self.assertEqual(1.0, length((1, 0), (0, 0)))

    def test_len_null(self):
        self.assertEqual(0.0, length((0, 0), (0, 0)))

    def test_len_nonnegative(self):
        x = randint(-100, 100)
        y = randint(-100, 100)
        a = randint(-100, 100)
        b = randint(-100, 100)
        self.assertTrue(length((x, y), (a, b)) >= 0.0)

    def test_len_symmetry(self):
        x = randint(-100, 100)
        y = randint(-100, 100)
        a = randint(-100, 100)
        b = randint(-100, 100)
        self.assertEqual(length((x, y), (a, b)), length((a, b), (x, y)))

    def test_len_triangle(self):
        x = randint(-100, 100)
        y = randint(-100, 100)
        a = randint(-100, 100)
        b = randint(-100, 100)
        c = randint(-100, 100)
        d = randint(-100, 100)
        self.assertTrue(length((x, y), (a, b)) <= length((x, y), (c, d)) + length((c, d), (a, b)))

    def test_common_side_part_fromStart(self):
        self.assertEqual(1, common_side(((0, 0), (1, 0)), ((0, 0), (2, 0))))

    def test_common_side_part_middle(self):
        self.assertEqual(1, common_side(((1, 0), (2, 0)), ((0, 0), (3, 0))))

    def test_common_side_part_toFinnish(self):
        self.assertEqual(1, common_side(((0, 0), (2, 0)), ((1, 0), (2, 0))))

    def test_common_side_negative(self):
        self.assertEqual(1, common_side(((-2, 0), (-0.5, 0)), ((-1.5, 0), (0, 0))))

    def test_common_side_symmetry(self):
        self.assertEqual(common_side(((-2, 0), (-0.5, 0)), ((-1.5, 0), (0, 0))),
                         common_side(((-1.5, 0), (-0, 0)), ((-2, 0), (-0.5, 0))))

    def test_subcontract(self):
        self.assertEqual(1, subcontract(
            (((0, 0), (0, 1)), ((0, 1), (1, 1)), ((1, 1), (1, 0)), ((1, 0), (0, 0))),
            (((0, 0), (0, 1)), ((0, 1), (-1, 1)), ((-1, 1), (-1, 0)), ((-1, 0), (0, 0)))))


start = unittest.TestSuite()
start.addTest(unittest.makeSuite(Test))
